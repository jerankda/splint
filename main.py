from linter import SimpleLinter

def main():
    with open('example_code.py', 'r') as file:
        code = file.read()

    linter = SimpleLinter(code)

    print(linter.check_syntax())
    print(linter.check_indentation())
    print(linter.check_line_length())
    print(linter.check_naming_conventions())
    print(linter.check_unused_imports())
    print(linter.check_docstrings())
    print(linter.check_magic_numbers())
    print(linter.check_formatting())
    print(linter.check_code_complexity())
    print(linter.check_deprecated_functions())
    print(linter.check_type_hints())
    print(linter.check_magic_methods())

if __name__ == "__main__":
    main()
