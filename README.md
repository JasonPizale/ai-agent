# AI AGENT
A brief description of what this agent does, the problems it solves, and how it works at a high level.

## Features
- Summarize key capabilities
- Bug fixing / refactoring / feature additions
- Tool usage (filesystem, code execution, etc.)
- Model/provider support

## Demo
- Screenshots or terminal GIFs (optional)

## Architecture
- Language: Python 3.11+
- Key libs: openai/google-generativeai/anthropic, pydantic, typer, etc.
- Structure:
  - `src/` – core agent logic
  - `tools/` – function-calling tools
  - `configs/` – model and runtime configs
  - `tests/` – unit/integration tests
  - `main.py` – entry point

## Getting Started

### Prerequisites
- Python 3.11+
- pip or uv/poetry
- API keys:
  - `OPENAI_API_KEY` or `GOOGLE_API_KEY` or `ANTHROPIC_API_KEY`
