# OMK Python Project Template

[![Made With Love](https://img.shields.io/badge/Made%20With-Love-orange.svg?style=for-the-badge)](https://github.com/chetanraj/awesome-github-badges) ![py_version](https://img.shields.io/badge/python-^3.11-blue?style=for-the-badge&logo=python&logoColor=9cf) ![version](https://img.shields.io/badge/version-0.1.0-gree?style=for-the-badge&logo=semver) ![code quality](https://img.shields.io/badge/code_quality-A-51C62B?style=for-the-badge&logo=codeforces&logoColor=9cf)

```text
   ____  __    __  ___      __ __          __   
  / __ \/ /_  /  |/  /_  __/ //_/___  ____/ /__ 
 / / / / __ \/ /|_/ / / / / ,< / __ \/ __  / _ \
/ /_/ / / / / /  / / /_/ / /| / /_/ / /_/ /  __/
\____/_/ /_/_/  /_/\__, /_/ |_\____/\__,_/\___/ 
                  /____/                                                                                                      
```

A clean, modern, and well-structured Python project template inspired by the **OhMyKode** approach:  
**Observe → Model → Kodify**

A simple, powerful, and intuitive workflow to build better Python projects:

- **Observe** the problem deeply and clearly  
- **Model** the underlying logic, structure or mathematics  
- **Kodify** the solution cleanly, using modern engineering practices  

This template helps you start projects the way engineers do:  
reproducible, modular, configurable, and easy to maintain.

---

## 🧭 OhMyKode Philosophy

The OMK methodology is the guiding flow behind this template:

### **🧠 Observe — understand deeply**
Break down the problem.  
Identify patterns, constraints, and structure.  
Clarify the “why” before touching the keyboard.

### **🧩 Model — structure clearly**
Translate intuition into a clean architecture.  
Use configuration, modular code, and clear separation of concerns.  
Make each part easy to test, extend, and reason about.

### **⌨️ Kodify — implement cleanly**
Implement the solution cleanly, with clarity, structure, and reproducibility in mind.

---

## 💡 Why this template?

Most Python projects begin with a single `script.py` that grows until it becomes unmaintainable.  
This template shows how to structure a project like a real engineer:

- A dedicated place for **source code**
- A clean area for **data**
- Separate zones for **notebooks**, **configs**, **tests**
- Proper handling of **logs**, **models**, and **documentation**

➡️ A clear structure leads to clear thinking — and cleaner code.

---

## ✨ Features

- **Modern Python stack**: [`uv`](https://github.com/astral-sh/uv), [`hydra`](https://github.com/facebookresearch/hydra), [`loguru`](https://github.com/Delgan/loguru)
- **Clear, scalable folder structure**
- **Hydra‑powered configuration** for reproducible experiments
- **Isolated logs, outputs, and models per run**
- **Makefile shortcuts** for a consistent developer experience
- **Tools included** to keep your project clean and maintainable
- **Beginner‑friendly**, no unnecessary complexity

---

## 🗂️ Project Structure

```text
.
├── conf/                # Hydra configuration (main config + groups)
│   ├── config.yaml
│   ├── data/default.yaml
│   ├── model/default.yaml
│   └── pipeline/default.yaml
│
├── src/
│   ├── core/            # Main logic: algorithms, pipelines, workflows
│   └── data/            # Data helpers (optional)
│
├── data/
│   ├── input/           # Raw, immutable input data
│   └── output/          # Processed or generated outputs
│
├── models/              # Saved models or artifacts
├── notebooks/           # Exploratory notebooks & experimentation
├── logs/                # Logs automatically created per run
├── tests/               # Unit/integration tests
├── docs/                # Documentation, diagrams, architecture notes
│
├── tools/               # Project maintenance utilities
│   ├── debug_env.py     # Show environment + config + deps
│   ├── clean_cache.py   # Clean Python caches (cross‑platform)
│   └── helpers.py       # Shared utility helpers dedicated to internal tooling scripts
│
├── main.py              # Project entrypoint (Hydra-powered)
├── Makefile             # Automation of common tasks
├── pyproject.toml       # Project configuration and dependencies (uv)
├── uv.lock              # Fully pinned dependency list
└── CHANGELOG            # Version tracking
```

Why this structure?

- **Each directory has ONE clear purpose**
- **Code, config, data, and logs are cleanly separated**
- **Scales smoothly from small scripts to real ML pipelines**
- **Matches modern engineering practice (ML, data, automation, research)**

---

## 🚀 Getting Started

This template uses [**uv**](https://github.com/astral-sh/uv), a fast, modern Python package manager.

```bash
git clone https://github.com/OhMyKode/omk-python-project-template
cd omk-python-project-template
uv sync
make run
```

Once the packages are installed, you can refer to the Makefile for all the available commands:

- **cloc**: Count lines of code using cloc (must be installed first)
- **format**: Format code with black and ruff
- **help**: List available commands
- **lock**: Update poetry.lock file
- **major**: Bump major version without committing
- **minor**: Bump minor version without committing
- **notebook**: Launch Jupyter notebook.
- **patch**: Bump patch version without committing
- **quality**: Check code quality metrics with radon
- **reqs**: Export dependencies to requirements.txt. Do not edit it manually
- **run**: Run the main script.
- **set-version**: Usage: make set-version version=1.2.3
- **show-version**: Show project's version
- **test**: Run unit tests
- **upgrade**: Upgrade all dependencies to their latest versions

**Principle:**  
> Makefile provides stable, memorable commands, so anyone should be able to run and explore the project with one command.

**P.S:** You can install `make` on Windows using Scoop or just copy paste the commands from file and execute them in the terminal.

---

## ⚙️ Configuration with Hydra

All configurable parameters live in:

```text
conf/
├── config.yaml
├── data/default.yaml
├── model/default.yaml
└── pipeline/default.yaml
```

Hydra enables:

### ✔ Reproducible runs  
Every run gets its own **timestamped directory** with:

- logs  
- configs used  
- outputs  

### ✔ Clean code  
No hard‑coded paths or values inside Python files.

### ✔ Easy experimentation  
Override parameters without modifying code.

---

## 🎯 Code Quality Metrics

You can quickly check the overall quality of the codebase using:

```sh
make quality
```

This command runs Radon, which calculates several helpful metrics:

- **Cyclomatic Complexity (cc)** : Measures how many decision paths a function has.
  More branches → harder to read and test. *Lower is better.*.
- **Maintainability Index (mi)**: Gives a score (0–100) estimating how easy the code is to understand and modify. *Higher is better*.
- **Halstead Metrics (hal)**: Analyze the “effort” required to read and understand the code based on operators and operands. It’s not something you need to memorize — it simply highlights code that might be too dense.

These metrics help you spot:

- functions that are becoming too complex
- code that may be hard to maintain later
- opportunities to simplify or refactor

Use make quality as a friendly guide to keep the code clean and easy to work with — especially as the project grows.

---

## 🧺 Notebooks

All exploratory work goes here:

- EDA
- prototyping
- sketches
- rapid experiments

Notebooks **should not modify the source code** directly.

---

## 📚 Documentation (`docs/`)

Use this folder for:

- architecture diagrams  
- explanations  
- learning notes  
- model descriptions  
- internal documentation  

---

## 🔄 Workflow & Pipeline

This template encourages a **clear and intentional** Git history.

### ✔ Branch per idea

```text
feat/add-training-step
fix/data-path
refactor/pipeline-cleanup
```

**Principle:**  
> Each change has a purpose and a name.


### ✔ Commit messages tell a short story
Use clean prefixes (Inspired by [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)):

``` sh
- :feat:          feat: a new feature
- :fix:           fix: a bug fix
- :docs:          docs: documentation only changes
- :style:         style: changes that do not affect the meaning of the code
                  (white-space, formatting, missing semi-colons, etc)
- :refactor:      refactor: a code change that neither fixes a bug nor adds a feature
- :perf:          perf: a code change that improves performance
- :test:          test: adding missing or correcting existing tests
- :chore:         chore: changes to the build process or auxiliary 
                  tools and libraries such as documentation generation
- :chore-release: chore(release): code deployment or publishing to external repositories
- :chore-deps:    chore(deps): add or delete dependencies
- :build:         build: changes related to build processes
- :ci:            ci: updates to the continuous integration system
- :config:        config: Changing configuration files.
- :security:      security: Fixing security issues.
```

Examples:

```text
feat: add basic pipeline runner
refactor: isolate data loader
fix: correct output directory path
```

**Principle:**  
> Your future self should understand your past decisions instantly.


## 🔢 Versioning Philosophy (Simple Semantic Versioning)

The template uses `MAJOR.MINOR.PATCH` ([semantic versioning](https://semver.org/)):

- **MAJOR** — breaking changes  
- **MINOR** — new features
- **PATCH** — small fixes, polish

Update automatically using:

```bash
make major
make minor
make patch
```

**P.S**: Project's version should not be edited manually. To set a specific project's version, use `make set-version` available command.

**Principle:**  
> Version numbers communicate change impact clearly and honestly.

---

## 📎 Links

- 📺 YouTube: <https://youtube.com/@OhMyKode>  
- 🐙 GitHub: <https://github.com/ohmykode>  
- 📨 Contact: <ohmykode@gmail.com>  

---

## 📄 License

This project is licensed under the **MIT License** (see `LICENSE` file).
