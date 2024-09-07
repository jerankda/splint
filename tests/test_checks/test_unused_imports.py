# tests/test_checks/test_unused_imports.py

import unittest
from checks.unused_imports import check_unused_imports

class TestUnusedImportsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "import os",
            "def example_function():",
            "    pass",
        ]

    def test_check_unused_imports(self):
        result = check_unused_imports(self.code)
        self.assertEqual(result, "Unused imports: os")

if __name__ == '__main__':
    unittest.main()
