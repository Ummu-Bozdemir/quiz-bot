Quiz-Bot

A simple Python project created in GitHub Codespaces.
It includes a basic greeting function, automated tests using pytest, and a configured ruff linter.
The goal is to demonstrate a clean project structure and basic development workflow.

Project Structure
.
├── README.md
├── pyproject.toml
├── pytest.ini
├── src
│   ├── __init__.py
│   └── main.py
└── tests
    ├── __init__.py
    └── test_main.py

Running the Application
uv run python src/main.py

Running Tests
uv run pytest

Running the Linter
uv run ruff check .

Overview

This project contains a small function that returns a greeting message.
A simple unit test is included to verify the behavior.
The repository was created as part of an introductory assignment to practice using Codespaces, uv, pytest, and ruff.