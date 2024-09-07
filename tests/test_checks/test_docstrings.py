# tests/test_checks/test_docstrings.py

import unittest
from checks.docstrings import check_docstrings

class TestDocstringsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    pass",
        ]

    def test_check_docstrings(self):
        result = check_docstrings(self.code)
        self.assertEqual(result, "All functions, classes, and modules have docstrings.")

if __name__ == '__main__':
    unittest.main()
