import ast

def check_type_hints(code):
    errors = []
    tree = ast.parse("\n".join(code))

    class TypeHintVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_FunctionDef(self, node):
            # Check for argument type hints
            for arg in node.args.args:
                if not arg.annotation:
                    self.errors.append(f"Function '{node.name}' on line {node.lineno} is missing type hint for argument '{arg.arg}'.")
            # Check for return type hint
            if node.returns is None:
                self.errors.append(f"Function '{node.name}' on line {node.lineno} is missing a return type hint.")

    TypeHintVisitor().visit(tree)
    return errors if errors else "All functions have type hints."
