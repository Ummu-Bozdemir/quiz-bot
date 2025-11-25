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
A unit test is included to verify the expected behavior.
The repository was prepared as part of an introductory assignment to practice working with Codespaces, uv, pytest, and ruff.