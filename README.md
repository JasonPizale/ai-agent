# AI AGENT
Short description of what your agent does and the problems it solves.

## Features
- Bug fixing / refactoring / feature additions
- File inspection and edits
- Run Python files and report results
- Configurable model/provider

## Architecture
- Language: Python 3.11+
- Key libs: pydantic, typer (adjust as needed)
- Structure:
  - `main.py` – CLI/entry point
  - `config.py` – configuration and environment
  - `functions/` – tool functions
    - `call_function.py`
    - `get_file_content.py`
    - `get_files_info.py`
    - `run_python_file.py`
    - `write_file.py`
  - `calculator/`
    - `README.md`, `lorem.txt`, `main.py`, `tests.py`
    - `pkg/`
      - `calculator.py`, `morelorem.txt`, `render.py`
  - `tests.py` – root tests (if separate from calculator/tests.py)
  - `pyproject.toml`, `uv.lock`
  - `.python-version`, `.gitignore`, `README.md`
