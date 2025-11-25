Quiz-Bot

This project is a simple Python application created in GitHub Codespaces.
It includes a basic greeting function, automated tests using pytest, and a configured ruff linter.
The goal is to demonstrate a clean project structure and basic tooling.

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

The project contains a simple function that returns a greeting message.
A unit test is included to verify the behavior.
This repository was prepared as part of an introductory assignment to practice working with Codespaces, uv, pytest, and ruff.