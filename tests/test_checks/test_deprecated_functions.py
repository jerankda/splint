# tests/test_checks/test_deprecated_functions.py

import unittest
from checks.deprecated_functions import check_deprecated_functions

class TestDeprecatedFunctionsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    pass",
        ]

    def test_check_deprecated_functions(self):
        result = check_deprecated_functions(self.code)
        self.assertEqual(result, "No deprecated functions found.")

if __name__ == '__main__':
    unittest.main()
