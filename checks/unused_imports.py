import ast

def check_unused_imports(code):
    tree = ast.parse("\n".join(code))
    imports = set()
    used = set()

    class ImportVisitor(ast.NodeVisitor):
        def __init__(self):
            self.imports = imports
            self.used = used

        def visit_Import(self, node):
            for alias in node.names:
                self.imports.add(alias.name)

        def visit_ImportFrom(self, node):
            for alias in node.names:
                self.imports.add(alias.name)

        def visit_Name(self, node):
            self.used.add(node.id)

    ImportVisitor().visit(tree)
    unused = imports - used
    return (f"Unused imports: {', '.join(unused)}" if unused else "No unused imports found.")
