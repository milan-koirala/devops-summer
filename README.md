# 🔢 Python Calculator

This is a simple, medium-level Python calculator project with:

## ✅ Features

- Basic operations: `add`, `subtract`, `multiply`, `divide`, `power`, `modulus`
- Interactive CLI using simple `input()` prompts
- Automated tests using `pytest`
- Code style checking using `flake8`
- Pre-commit hooks for linting and testing
- CI workflow with GitHub Actions (multi-version Python support)

---

## 🚀 Usage

Run the CLI:

### 🧪 Running Tests

```bash
pytest
```
Or with verbose output:
```bash
pytest -v
```

### 🔍 Code Quality Checks
Lint Python code using **flake8**:
```bash
flake8 src/
```

---

### 🔁 Pre-commit Setup
To install and enable pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```
Now every commit will automatically:
- Run flake8 on src/
- Run all pytest tests in tests/

---

### 📦 Project Metadata
Project configuration is defined in:
- pyproject.toml
- pytest.ini
- .pre-commit-config.yaml

---

## 🤖 CI/CD
A GitHub Actions workflow is configured to:
- Run linting with flake8
- Run tests using pytest
- Check compatibility with Python 3.9, 3.10, and 3.11
