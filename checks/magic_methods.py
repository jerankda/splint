import ast

def check_magic_methods(code):
    errors = []
    tree = ast.parse("\n".join(code))

    class MagicMethodVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_ClassDef(self, node):
            methods = {m.name for m in node.body if isinstance(m, ast.FunctionDef)}
            required_methods = {'__init__', '__str__', '__repr__'}
            missing_methods = required_methods - methods
            for method in missing_methods:
                self.errors.append(f"Class '{node.name}' on line {node.lineno} is missing a '{method}' method.")

    MagicMethodVisitor().visit(tree)
    return errors if errors else "All classes have the necessary magic methods."
