# Quiz-Bot

A simple Python project created in GitHub Codespaces.  
It includes a small greeting function, automated tests using pytest, and a configured ruff linter.  
The goal is to practice clean project structure, testing, and basic development workflow.

---

## Project Structure

```
quiz-bot/
├── README.md
├── pyproject.toml
├── pytest.ini
├── src
│ ├── init.py
│ └── main.py
└── tests
├── init.py
└── test_main.py
```

---

## Application Entry Point

The main function returns a greeting message:

def hello() -> str:
return "Hello, World!"


Run the application with:

uv run python src/main.py


---

## Running Tests

Run the test suite with:

uv run pytest


---

## Linting (ruff)

Check code style with:

uv run ruff check .


---

## Overview

This project contains a simple function and a small unit test validating its behavior.  
It was created as part of an introductory assignment to practice working with Codespaces, uv, pytest, and ruff.
