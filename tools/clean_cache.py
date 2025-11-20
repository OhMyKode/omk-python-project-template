# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

from helpers import colored

# directories and file extensions to remove
REMOVE_DIRS = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".ipynb_checkpoints",
]

# compiled Python file extensions to remove
REMOVE_EXTS = (".pyc", ".pyo")


def main(verbose: bool = True) -> None:
    """Clean up Python cache files and directories.

    Parameters
    ----------
    verbose : bool, optional
        Whether to print detailed information during cleanup, by default True
    """
    # get the root directory (current working directory)
    root = Path(".").resolve()

    print(colored(f"🧹 Starting Python cache cleanup in: {root}", "36"))

    # counts for summary
    removed_dirs = 0
    removed_files = 0

    # remove cache directories
    print(colored("Scanning for cache directories...", "33"))
    for cache_dir in REMOVE_DIRS:
        for path in root.rglob(cache_dir):
            if path.is_dir():
                removed_dirs += 1
                shutil.rmtree(path, ignore_errors=True)

    # remove compiled Python files
    print(colored("Scanning for .pyc/.pyo files...", "33"))
    for ext in REMOVE_EXTS:
        for path in root.rglob(f"*{ext}"):
            if path.is_file():
                removed_files += 1
                try:
                    path.unlink()
                except OSError:
                    pass

    # summary section of removed items
    print(colored("\nCleanup summary:", "34"))
    print(colored(f"  - Directories removed: {removed_dirs}", "32"))
    print(colored(f"  - Files removed:       {removed_files}", "32"))

    print(colored("\n✨ Cleanup completed successfully!\n", "92"))


if __name__ == "__main__":
    main()
