# utils/ast_utils.py

import ast

def get_functions(tree):
    """Return all function definitions in the AST."""
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def get_classes(tree):
    """Return all class definitions in the AST."""
    return [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

def get_imports(tree):
    """Return all imports in the AST."""
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                imports.add(alias.name)
    return imports
