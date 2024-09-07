# utils/formatting.py

def check_formatting(code):
    errors = []
    for i, line in enumerate(code, start=1):
        if '  ' in line:  # Detects multiple spaces
            errors.append(f"Line {i} contains multiple spaces.")
        if not line.strip():  # Checks for unnecessary blank lines
            errors.append(f"Empty line at {i}.")
    return errors if errors else "Code formatting is consistent."
