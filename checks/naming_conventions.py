import ast
import re

def check_naming_conventions(code):
    errors = []
    snake_case_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
    camel_case_pattern = re.compile(r'^[a-z][a-zA-Z0-9]*$')
    constant_case_pattern = re.compile(r'^[A-Z][A-Z0-9_]*$')
    tree = ast.parse("\n".join(code))

    class NamingVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_FunctionDef(self, node):
            if not snake_case_pattern.match(node.name):
                self.errors.append(f"Function name '{node.name}' on line {node.lineno} should be snake_case.")
            
        def visit_ClassDef(self, node):
            if not snake_case_pattern.match(node.name):
                self.errors.append(f"Class name '{node.name}' on line {node.lineno} should be snake_case.")
        
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store) and not camel_case_pattern.match(node.id):
                self.errors.append(f"Variable name '{node.id}' on line {node.lineno} should be camelCase.")
            if isinstance(node.ctx, ast.Load) and not constant_case_pattern.match(node.id):
                self.errors.append(f"Constant name '{node.id}' on line {node.lineno} should be CONSTANT_CASE.")

    NamingVisitor().visit(tree)
    return errors if errors else "All names follow naming conventions."
