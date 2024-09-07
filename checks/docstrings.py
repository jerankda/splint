import ast

def check_docstrings(code):
    errors = []
    tree = ast.parse("\n".join(code))

    class DocstringVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_FunctionDef(self, node):
            if ast.get_docstring(node) is None:
                self.errors.append(f"Function '{node.name}' on line {node.lineno} is missing a docstring.")
            
        def visit_ClassDef(self, node):
            if ast.get_docstring(node) is None:
                self.errors.append(f"Class '{node.name}' on line {node.lineno} is missing a docstring.")

        def visit_Module(self, node):
            if ast.get_docstring(node) is None:
                self.errors.append("Module is missing a docstring.")

    DocstringVisitor().visit(tree)
    return errors if errors else "All functions, classes, and modules have docstrings."
