# Antigravity Skills Project

A demonstration and test environment for various developer agent skills, including database schema validation, license header formatting, Git commit message checking, and JSON-to-Pydantic conversion.

## Repository Structure

* **`git_test/`**: A test directory containing the authentication module [auth.py](git_test/auth.py).
* **`my_script.py`**: A simple Python hello-world script prepended with the Apache 2.0 license.
* **`product.json` / `product_model.py`**: A sample JSON data file and its corresponding Pydantic schema model.
* **`bad_schema.sql`**: A sample SQL schema file designed to test validation checks for safety and styling policies.
* **`.agents/skills/`**: Custom agent skills:
  * `database-schema-validator`: Validates SQL safety, naming, and structural policies.
  * `git-commit-formatter`: Formats commit messages following the Conventional Commits specification.
  * `json-to-pydantic`: Translates JSON objects into Pydantic model classes.
  * `license-header-adder`: Automated open-source copyright/license header injection.

## Setup

This repository uses a Python virtual environment to manage dependencies locally.

### 1. Initialize Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

### 2. Configure Editor (VS Code / Cursor)
The project includes a `.vscode/settings.json` and a `pyrightconfig.json` at the root directory to automatically route your language server/interpreter to the local virtual environment. 

---
*Created and maintained as a pair programming workspace.*
