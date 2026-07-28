import sys

# Simulate a piece of code that a developer might write.
# This code contains issues that our "assistants" will check.
sample_code = """
def calculateTotal(item_price, quantity): # CamelCase function name - issue for silent hook
    total = item_price * quantity
    print("Calculating total...") # Print statement - issue for noisy hook
    return total

def process_order(order_id):
    # Some processing logic
    result = calculateTotal(10, 5)
    print(f"Order {order_id} processed. Total: {result}") # Another print statement
    return True

if __name__ == "__main__":
    process_order("ORD-123")
"""

def silent_observer_check(code_content):
    """
    Simulates a 'silent hook' or 'observer' assistant.
    It identifies potential style issues (e.g., camelCase function names)
    and reports them without blocking execution. This is like a linter suggesting improvements.
    """
    print("--- Silent Observer Check (Linter-like) ---")
    warnings_found = 0
    lines = code_content.splitlines()
    for i, line in enumerate(lines):
        # Check for camelCase function definitions
        if line.strip().startswith("def ") and "(" in line:
            func_name_start = line.find("def ") + 4
            func_name_end = line.find("(")
            if func_name_start < func_name_end:
                func_name = line[func_name_start:func_name_end].strip()
                # Simple check for camelCase (starts with lowercase, contains uppercase, no underscores)
                if func_name and func_name[0].islower() and any(c.isupper() for c in func_name[1:]) and '_' not in func_name:
                    print(f"WARNING: Line {i+1}: Function '{func_name}' might not follow snake_case convention.") # Illustrates 'silent hook' feedback
                    warnings_found += 1
    if warnings_found == 0:
        print("No style warnings found by silent observer.")
    print("Silent observer check complete. Execution continues.")
    print("-" * 50)

def noisy_teacher_check(code_content):
    """
    Simulates a 'noisy hook' or 'teacher' assistant.
    It enforces critical rules (e.g., no print statements in production code)
    and blocks execution if a violation is found. This is like a pre-commit hook or a strict build check.
    """
    print("--- Noisy Teacher Check (Pre-commit/Enforcement-like) ---")
    errors_found = 0
    lines = code_content.splitlines()
    for i, line in enumerate(lines):
        # Check for 'print(' statements, which might be disallowed in production
        if "print(" in line and not line.strip().startswith("#"): # Ignore commented out prints
            print(f"ERROR: Line {i+1}: Prohibited 'print()' statement found!") # Illustrates 'noisy hook' enforcement
            errors_found += 1

    if errors_found > 0:
        print(f"Noisy teacher found {errors_found} critical error(s). Blocking execution.")
        print("-" * 50)
        sys.exit(1) # Block execution - the core of 'noisy teacher'
    else:
        print("No critical errors found by noisy teacher.")
        print("Noisy teacher check complete. Execution continues.")
    print("-" * 50)


if __name__ == "__main__":
    print("Simulating a development workflow with coding assistants.\n")

    # Step 1: Run the silent observer check
    # This check identifies potential issues but allows the process to continue.
    silent_observer_check(sample_code)

    # Step 2: Run the noisy teacher check
    # This check enforces critical rules and will stop the process if violated.
    try:
        noisy_teacher_check(sample_code)
        print("\nAll checks passed. Code is ready for deployment/commit.")
        # In a real scenario, the code might be executed or committed here.
        print("\n--- Executing the (simulated) code ---")
        # For demonstration, we'll just print it, but imagine it runs.
        # exec(sample_code) # Would actually run the code
        print("Sample code content:\n" + sample_code)

    except SystemExit:
        print("\nWorkflow halted due to critical errors found by the noisy teacher.")
        print("Please fix the issues before proceeding.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
