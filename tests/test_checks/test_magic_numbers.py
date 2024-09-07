# tests/test_checks/test_magic_numbers.py

import unittest
from checks.magic_numbers import check_magic_numbers

class TestMagicNumbersCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    pass",
        ]

    def test_check_magic_numbers(self):
        result = check_magic_numbers(self.code)
        self.assertEqual(result, "No magic numbers found.")

if __name__ == '__main__':
    unittest.main()
