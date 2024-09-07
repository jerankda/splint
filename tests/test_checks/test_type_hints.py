# tests/test_checks/test_type_hints.py

import unittest
from checks.type_hints import check_type_hints

class TestTypeHintsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function(param):",
            "    return param",
        ]

    def test_check_type_hints(self):
        result = check_type_hints(self.code)
        self.assertEqual(result, "All functions have type hints.")

if __name__ == '__main__':
    unittest.main()
