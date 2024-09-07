import ast

def check_magic_numbers(code):
    errors = []
    tree = ast.parse("\n".join(code))

    class MagicNumberVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and not (0 <= node.value <= 1000):  # Adjust range as needed
                self.errors.append(f"Magic number '{node.value}' found on line {node.lineno}. Consider using a named constant.")

    MagicNumberVisitor().visit(tree)
    return errors if errors else "No magic numbers found."
