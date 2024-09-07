# tests/test_checks/test_indentation.py

import unittest
from checks.indentation import check_indentation

class TestIndentationCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    pass",
        ]

    def test_check_indentation(self):
        result = check_indentation(self.code)
        self.assertEqual(result, "Indentation is valid.")

if __name__ == '__main__':
    unittest.main()
