# Splint

A fast, simple, and easy-to-use Python linter.

![Build Status](https://github.com/jerankda/splint/actions/workflows/python-publish.yml/badge.svg)
![License](https://img.shields.io/github/license/jerankda/splint)
![Version](https://img.shields.io/pypi/v/splint)


##Splint is a Python linter designed to help you catch common issues, enforce coding standards, and improve your Python code.

> ⚠️ **Note:** Splint is currently in early development

---

## Installation

```bash
pip install splint
```
## Features

### Working Features:
- **Syntax Checking**: Validates Python code syntax using `ast.parse`.
- **Indentation Checking**: Ensures correct indentation levels and alignment.
- **Line Length Checking**: Verifies that lines do not exceed a specified length.
- **Naming Conventions Checking**: Enforces snake_case for functions and classes, camelCase for variables, and CONSTANT_CASE for constants.
- **Unused Imports Checking**: Identifies and reports unused imports.
- **Docstrings Checking**: Ensures all functions, classes, and modules have docstrings.
- **Magic Numbers Checking**: Detects and flags "magic numbers" that are outside a specified range.
- **Code Complexity Checking**: Estimates complexity based on decision points within functions.
- **Deprecated Functions Checking**: Flags usage of deprecated functions.

### Not Yet Implemented:
- **Single Responsibility Principle Checking**: Analysis to ensure that each function or class adheres to the Single Responsibility Principle.
- **Formatting Checking**: Comprehensive checks for adherence to PEP8 formatting standards, including code style and formatting rules.
- **Cyclomatic Complexity Checking**: Analysis of cyclomatic complexity to measure the number of linearly independent paths through the code.
- **Magic Methods Checking**: Verification for the presence and proper implementation of common Python magic methods.
- **PEP8 Compliance**: Full compliance with PEP8 style guide for Python code.
- **Code Smells Detection**: Identification of common code smells that may indicate potential issues or areas for improvement.
- **Documentation Coverage Checking**: Verification to ensure that code is adequately documented.
- **Refactoring Opportunities Checking**: Detection of potential areas in the code that may benefit from refactoring.
- **Performance Checking**: Analysis to identify potential performance bottlenecks and optimizations.
- **Security Vulnerabilities Checking**: Identification of potential security vulnerabilities in the code.



## Usage

To use **Splint**, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/jerankda/splint
   cd simple_linter
   ```
2. **Install Dependencies:**
   ```
   pip install -r requirements.txt"
   ```
3. **Run the Linter:**
   ```
   python main.py <path-to-your-python-file>
   ```
   Replace <path-to-your-python-file> with the path to the Python file you want to lint.
