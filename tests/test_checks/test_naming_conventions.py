# tests/test_checks/test_naming_conventions.py

import unittest
from checks.naming_conventions import check_naming_conventions

class TestNamingConventionsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    pass",
        ]

    def test_check_naming_conventions(self):
        result = check_naming_conventions(self.code)
        self.assertEqual(result, "All names follow naming conventions.")

if __name__ == '__main__':
    unittest.main()
