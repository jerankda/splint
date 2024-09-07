# linter.py

import ast
from checks.indentation import check_indentation
from checks.naming_conventions import check_naming_conventions
from checks.docstrings import check_docstrings
from checks.magic_numbers import check_magic_numbers
from checks.unused_imports import check_unused_imports
from checks.type_hints import check_type_hints
from checks.complexity import check_code_complexity
from checks.magic_methods import check_magic_methods
from checks.deprecated_functions import check_deprecated_functions
from utils.formatting import check_formatting

class SimpleLinter:
    def __init__(self, code):
        self.code = code.splitlines()

    def check_syntax(self):
        try:
            ast.parse("\n".join(self.code))
            return "Syntax is valid."
        except SyntaxError as e:
            return f"Syntax error: {e}"

    def check_indentation(self):
        return check_indentation(self.code)

    def check_line_length(self, max_length=79):
        errors = []
        for i, line in enumerate(self.code, start=1):
            if len(line) > max_length:
                errors.append(f"Line {i} exceeds {max_length} characters.")
        return errors if errors else "All lines are within the length limit."

    def check_naming_conventions(self):
        return check_naming_conventions(self.code)

    def check_unused_imports(self):
        return check_unused_imports(self.code)

    def check_docstrings(self):
        return check_docstrings(self.code)

    def check_magic_numbers(self):
        return check_magic_numbers(self.code)

    def check_single_responsibility(self):
        errors = []
        return "Single Responsibility Principle check is not yet implemented."

    def check_formatting(self):
        return check_formatting(self.code)

    def check_code_complexity(self):
        return check_code_complexity(self.code)

    def check_deprecated_functions(self):
        return check_deprecated_functions(self.code)

    def check_type_hints(self):
        return check_type_hints(self.code)

    def check_cyclomatic_complexity(self):
        errors = []
        return "Cyclomatic complexity check is not yet implemented."

    def check_magic_methods(self):
        return check_magic_methods(self.code)

    def check_pep8_compliance(self):
        errors = []
        return "PEP8 compliance check is not yet implemented."

    def check_code_smells(self):
        errors = []
        return "Code smell detection is not yet implemented."

    def check_documentation_coverage(self):
        errors = []
        return "Documentation coverage check is not yet implemented."

    def check_refactoring_opportunities(self):
        errors = []
        return "Refactoring opportunities check is not yet implemented."

    def check_performance(self):
        errors = []
        return "Performance check is not yet implemented."

    def check_security_vulnerabilities(self):
        errors = []
        return "Security vulnerability check is not yet implemented."
