import ast

def check_code_complexity(code):
    errors = []
    # Basic cyclomatic complexity approximation: counting decision points (e.g., `if`, `for`, `while`)
    tree = ast.parse("\n".join(code))

    class ComplexityVisitor(ast.NodeVisitor):
        def __init__(self):
            self.errors = errors

        def visit_FunctionDef(self, node):
            decision_points = 0
            for n in ast.walk(node):
                if isinstance(n, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
                    decision_points += 1
            if decision_points > 5:  # Adjust threshold as needed
                self.errors.append(f"Function '{node.name}' on line {node.lineno} has too many decision points ({decision_points}).")

    ComplexityVisitor().visit(tree)
    return errors if errors else "All functions are within complexity limits."
