# Mathematical Operations Library

This is a simple Python library that provides basic mathematical operations.

## Available Operations

The library provides the following mathematical operations:

1. **Addition** - Add two numbers together
2. **Subtraction** - Subtract one number from another
3. **Multiplication** - Multiply two numbers together
4. **Division** - Divide one number by another (with divide-by-zero error handling)

## Usage

```python
from test_branch import add, subtract, multiply, divide

# Addition
result = add(5, 3)  # Returns 8

# Subtraction
result = subtract(5, 3)  # Returns 2

# Multiplication
result = multiply(5, 3)  # Returns 15

# Division
result = divide(6, 3)  # Returns 2
# Note: Division by zero will raise a ZeroDivisionError
```

## Running Tests

The library includes unit tests for all operations. To run the tests:

```bash
python -m unittest test_branch.py
```

or simply:

```bash
python test_branch.py
```