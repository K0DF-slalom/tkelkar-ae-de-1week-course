---
name: generate_tests
description: Generate comprehensive pytest test cases for Python functions and modules.
---

# Generate Tests

## Purpose
Generate comprehensive test cases for Python functions using pytest.

## When to Use
Use this skill when you need to create tests for new or existing functions.

## Steps
1. Analyze the target function's parameters, return types, and behavior
2. Create a test file in the `tests/` directory with naming convention `test_<module_name>.py`
3. Generate the following test cases for each function
   - 2 happy path cases (typical valid inputs)
   - 2 edge cases (boundary conditions, empty inputs, etc.)
   - 1 error case (invalid inputs that should raise exceptions)
4. Use descriptive test function names: `test_<function>_<scenario>`
5. Include docstrings explaining what each test validates
6. Use pytest assertions (`assert`, `pytest.raises`)

## Success Criteria
- All 5 test types are present
- Tests follow naming conventions
- Each test has a clear docstring
- Tests are in the correct directory

## Example Test Structure
def test_calculate_total_with_valid_items():
    """Test that calculate_total correctly sums valid item prices."""
    # Test implementation