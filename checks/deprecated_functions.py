import ast

def check_deprecated_functions(code):
    errors = []
    deprecated_functions = {
        'old_function': 'use_new_function'
        # Add more deprecated functions and their replacements here
    }
    tree = ast.parse("\n".join(code))

    class DeprecatedVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id in deprecated_functions:
                self.errors.append(f"Deprecated function '{node.func.id}' used on line {node.lineno}. Consider using '{deprecated_functions[node.func.id]}'.")

    DeprecatedVisitor().visit(tree)
    return errors if errors else "No deprecated functions found."
