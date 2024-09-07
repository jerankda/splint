# tests/test_linter.py

import unittest
from linter import SimpleLinter

class TestSimpleLinter(unittest.TestCase):
    def setUp(self):
        self.code = """
def example_function():
    pass
"""
        self.linter = SimpleLinter(self.code)

    def test_check_syntax(self):
        result = self.linter.check_syntax()
        self.assertEqual(result, "Syntax is valid.")

    def test_check_indentation(self):
        result = self.linter.check_indentation()
        self.assertEqual(result, "Indentation is valid.")

    def test_check_line_length(self):
        result = self.linter.check_line_length(max_length=79)
        self.assertEqual(result, "All lines are within the length limit.")

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
