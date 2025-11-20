# Makefile

.DEFAULT_GOAL := help

version = 0.1.0


.PHONY: help run notebook test reqs lock cloc quality format patch minor major set-version show-version upgrade clean

help: ## Show this help message
	@echo "\n🚀 Available Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}'

run: ## Run the main script.
	@echo "🚀 Running the main script..."
	@uv run python main.py || { echo "❌ Application failed to run."; exit 1; }

notebook: ## Launch Jupyter notebook.
	@uv run jupyter notebook
	@echo "🧪 Launching Jupyter Notebook..."
	@uv run jupyter notebook || { echo "❌ Jupyter Notebook init failed"; exit 1; }

test: ## Run unit tests
	@echo "🧪 Running unit tests..."
	@uv run pytest -s -q --disable-pytest-warnings || { echo "❌ Unit tests failed"; exit 1; }
	@echo "✅ Unit tests passed."

reqs: ## Export dependencies to requirements.txt
	@echo "📦 Generating requirements.txt..."
	@uv export --no-hashes --all-groups -o requirements.txt || { echo "❌ Failed to generate requirements.txt"; exit 1; }
	@echo "✅ requirements.txt created."

lock: ## Update uv.lock file
	@echo "🔒 Locking dependencies..."
	@uv lock || { echo "❌ Failed to update uv.lock"; exit 1; }
	@echo "✅ uv.lock updated."

cloc: ## Count lines of code using cloc (must be installed first)
	@echo "📊 Counting lines of code..."
	@uv run cloc --exclude-dir .venv,.DS_Store --exclude-ext gif,pyc . || { echo "❌ cloc failed"; exit 1; }

quality: ## Check code quality metrics with radon
	@echo "🧹 Analyzing code quality metrics..."
	@uv run radon cc mi hal . -a -na -s || { echo "❌ radon failed"; exit 1; }

format: ## Format code with black and ruff
	@echo "🎨 Formatting code..."
	@uv run black . || { echo "❌ black formatting failed"; exit 1; }
	@uv run ruff check -e --unsafe-fixes --fix . || { echo "❌ ruff formatting failed"; exit 1; }

patch: ## Bump patch version without committing
	@uv run bump-my-version bump patch --allow-dirty

minor: ## Bump minor version without committing
	@uv run bump-my-version bump minor --allow-dirty

major: ## Bump major version without committing
	@uv run bump-my-version bump major --allow-dirty

set-version: ## Usage: make set-version version=1.2.3
	@uv run bump-my-version bump patch --new-version $(version) --allow-dirty

show-version: ## Show project's version
	@uv run bump-my-version show current_version

upgrade: ## Upgrade all dependencies to their latest versions
	@echo "⬆️ Upgrading all dependencies..."
	@uv lock --upgrade & uv sync || { echo "❌ Dependency upgrade failed"; exit 1; }
	@echo "✅ All dependencies upgraded."

debug: ## Debug the virtual environment setup.
	@uv run python tools/debug_env.py

clean: ## Clean cache and temporary files.
	@uv run python tools/clean_cache.py
