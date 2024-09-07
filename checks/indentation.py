def check_indentation(code):
    errors = []
    indent_stack = [0]
    for i, line in enumerate(code):
        stripped_line = line.lstrip()
        if stripped_line:
            indent_level = len(line) - len(stripped_line)
            if indent_level % 4 != 0:
                errors.append(f"Indentation error at line {i + 1}. Expected multiple of 4 spaces.")
            if indent_level > indent_stack[-1]:
                indent_stack.append(indent_level)
            elif indent_level < indent_stack[-1]:
                if indent_stack[-1] != indent_level:
                    errors.append(f"Indentation error at line {i + 1}. Mismatched indentation level.")
                indent_stack.pop()
    if len(indent_stack) != 1:
        errors.append(f"Indentation error: Unbalanced indentation levels.")
    return errors if errors else "Indentation is valid."
