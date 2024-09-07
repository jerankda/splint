# tests/test_checks/test_complexity.py

import unittest
from checks.complexity import check_code_complexity

class TestComplexityCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "def example_function():",
            "    for i in range(10):",
            "        if i % 2 == 0:",
            "            pass",
        ]

    def test_check_code_complexity(self):
        result = check_code_complexity(self.code)
        self.assertEqual(result, "All functions are within complexity limits.")

if __name__ == '__main__':
    unittest.main()
