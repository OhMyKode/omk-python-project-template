# -*- coding: utf-8 -*-

import os
import platform
import sys
import tomllib
from importlib import metadata
from pathlib import Path

from omegaconf import OmegaConf

# hydra is optional. If not installed, fall back to no-op.
try:
    from hydra import compose, initialize
except ImportError:
    compose = None
    initialize = None

from helpers import colored


def get_pkg_version(name: str) -> str:
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return "not installed"


def print_section(title: str) -> None:
    """Print a colored section title."""
    print(colored(f"\n=== {title} ===", "36"))  # cyan


def parse_requirements(req: str) -> str:
    """
    Extract package name from a PEP 508 requirement string.

    Examples:
        'numpy>=1.26.0'   -> 'numpy'
        'pandas[perf]'    -> 'pandas'
        'torch==2.2.0'    -> 'torch'
    """
    # Remove extras: pandas[perf] -> pandas
    base = req.split("[", 1)[0]
    # Remove version specifiers: numpy>=1.26.0 -> numpy
    for sep in (">=", "<=", "==", "~=", "!=", ">", "<"):
        base = base.split(sep, 1)[0]
    return base.strip()


def load_dependency_groups(pyproject_path: Path) -> dict[str, list[str]]:
    """
    Load dependencies from pyproject.toml and group them by category.

    Supports:
    - 'main' -> project.dependencies
    - 'optional deps' -> project.optional-dependencies.<group>  (PEP 621)
    - 'dependency-groups.<group>' -> uv-style groups
    """
    if not pyproject_path.exists():
        return {}

    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    project = data.get("project", {})
    groups: dict[str, list[str]] = {}

    # Main dependencies (PEP 621)
    main_deps = project.get("dependencies", []) or []
    groups["main"] = [parse_requirements(d) for d in main_deps]

    # Optional dependencies (standard PEP 621)
    opt_deps = project.get("optional-dependencies", {}) or {}
    for group_name, deps in opt_deps.items():
        groups[group_name] = [parse_requirements(d) for d in deps]

    # uv-style dependency groups:
    dep_groups = data.get("dependency-groups", {}) or {}
    for group_name, deps in dep_groups.items():
        groups[group_name] = [parse_requirements(d) for d in deps]

    # Remove empty groups
    groups = {k: v for k, v in groups.items() if v}

    return groups


def print_hydra_config(project_root: Path) -> None:
    """Load and beautifully display the composed Hydra config from conf/."""
    print_section("Hydra Config (from conf/)")

    if initialize is None or compose is None:
        print(
            colored(
                "Hydra-core is not installed. Install it to inspect Hydra configs.",
                "33",
            )
        )
        return

    # debug_env.py is in tools/ → conf/ is one directory up
    script_dir = Path(__file__).parent
    conf_dir = script_dir.parent / "conf"

    if not conf_dir.exists():
        print(colored(f"conf/ directory not found at: {conf_dir}", "33"))
        return

    try:
        # config_path is relative to this script's location
        with initialize(config_path="../conf", version_base="1.3"):
            cfg = compose(config_name="config")
    except Exception as e:  # noqa: BLE001
        print(colored(f"Failed to load Hydra config: {e}", "31"))
        return

    # Header
    print(colored("- Config directory:", "35"), conf_dir)
    print(colored("- Loaded config name:", "35"), "config.yaml")

    # Top-level keys
    top_keys = sorted(cfg.keys())
    print(colored("\n🔑 Top-level configuration keys:", "34"))
    for k in top_keys:
        print(colored(f"  • {k}", "36"))

    # Pretty YAML preview
    print(colored("\nPreview of merged configuration:", "35"))

    yaml_str = OmegaConf.to_yaml(cfg, resolve=True)

    for line in yaml_str.split("\n"):
        # Highlight keys (lines with "key:" that are not list items)
        stripped = line.lstrip()
        if ":" in stripped and not stripped.startswith("-"):
            key_part = stripped.split(":", 1)[0]
            rest = stripped[len(key_part) :]
            indent_spaces = len(line) - len(stripped)
            indent_prefix = " " * indent_spaces
            colored_key = colored(key_part, "34")  # blue
            print("  " + indent_prefix + colored_key + rest)
        else:
            print("  " + colored(line, "37"))  # light gray for other lines

    # Hydra defaults list (if present)
    if hasattr(cfg, "defaults"):
        print(colored("\n📚 Active Hydra Defaults:", "35"))
        for entry in cfg.defaults:
            if isinstance(entry, dict):
                for group, value in entry.items():
                    print(colored(f"  ▸ {group}", "36") + f" = {value}")
            else:
                print(colored(f"  ▸ {entry}", "36"))

    print(colored("✨ Hydra config loaded successfully!\n", "32"))


def main() -> None:
    project_root = Path(".").resolve()
    cwd = Path.cwd().resolve()
    pyproject_path = project_root / "pyproject.toml"
    uv_lock = project_root / "uv.lock"

    print(colored("🧠 OMK Environment Debugger", "35"))

    # Python info
    print_section("Python")
    print(f"Executable : {sys.executable}")
    print(f"Version    : {sys.version.split()[0]}")
    print(f"Platform   : {platform.system()} {platform.release()} ({platform.machine()})")

    # Virtual env info
    print_section("Virtual Environment")
    venv = os.environ.get("VIRTUAL_ENV") or os.environ.get("CONDA_PREFIX")
    print(f"Active venv     : {venv if venv else 'none detected'}")
    print(f"sys.prefix      : {sys.prefix}")
    print(f"Project root    : {project_root}")
    print(f"Current workdir : {cwd}")

    # Dependencies from pyproject.toml
    print_section("Dependencies by group (from pyproject.toml)")

    if not pyproject_path.exists():
        print(colored("pyproject.toml not found, skipping dependency groups.", "33"))
    else:
        groups = load_dependency_groups(pyproject_path)
        if not groups:
            print(colored("No dependencies defined in pyproject.toml.", "33"))
        else:
            for group, pkgs in groups.items():
                print(colored(f"[Group: {group}]", "35"))
                for pkg in sorted(set(pkgs)):
                    version = get_pkg_version(pkg)
                    print(f"  {pkg:20} -> {version}")

        # Reference to uv.lock
        if uv_lock.exists():
            print(
                colored(
                    "\n📌 For detailed, pinned versions of all dependencies, see:",
                    "33",
                )
            )
            print(colored(f"   → {uv_lock}", "34"))
        else:
            print(
                colored(
                    "\n📌 No uv.lock found. Run `uv sync` to generate a lockfile.",
                    "33",
                )
            )

    # Generic environment variables (filtered)
    print_section("Selected Environment Variables")
    generic_keys = [
        "PYTHONPATH",
        "VIRTUAL_ENV",
        "CONDA_PREFIX",
        "UV_SYSTEM_PYTHON",
        "UV_PROJECT_ENVIRONMENT",
    ]
    for key in generic_keys:
        value = os.environ.get(key)
        if value:
            print(f"{key:25} = {value}")

    # Hydra config (pretty)
    print_hydra_config(project_root)

    print(colored("✅ Environment debug complete.\n", "32"))


if __name__ == "__main__":
    main()
