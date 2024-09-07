# tests/test_checks/test_magic_methods.py

import unittest
from checks.magic_methods import check_magic_methods

class TestMagicMethodsCheck(unittest.TestCase):
    def setUp(self):
        self.code = [
            "class ExampleClass:",
            "    def __init__(self):",
            "        pass",
        ]

    def test_check_magic_methods(self):
        result = check_magic_methods(self.code)
        self.assertEqual(result, "Class has magic methods as needed.")

if __name__ == '__main__':
    unittest.main()
