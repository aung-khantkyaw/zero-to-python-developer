# Module 8: Error and Exception Handling

**Goal:** Understand Python’s exception handling mechanism and learn to write robust programs that gracefully manage errors.

## 1. Introduction to Errors and Exceptions

In Python, there are two main types of errors:

### 1.1. Syntax Errors

Errors that occur when the parser encounters invalid syntax. These prevent the program from running.

```python
# SyntaxError: invalid syntax
print("Hello"
```

### 1.2. Exceptions (Runtime Errors)

Errors that occur during execution, even if the syntax is correct. They cause the program to stop unless handled.

```python
# ZeroDivisionError
result = 10 / 0

# NameError
print(undefined_variable)

# TypeError
"2" + 2
```

---

## 2. Common Built‑in Exceptions

| Exception           | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `ZeroDivisionError` | Division by zero.                                                                  |
| `NameError`         | Variable not defined.                                                              |
| `TypeError`         | Operation applied to object of wrong type.                                         |
| `ValueError`        | Function receives argument of correct type but invalid value (e.g., `int("abc")`). |
| `IndexError`        | Sequence index out of range.                                                       |
| `KeyError`          | Dictionary key not found.                                                          |
| `FileNotFoundError` | File does not exist.                                                               |
| `AttributeError`    | Object has no attribute.                                                           |
| `ImportError`       | Module not found.                                                                  |

---

## 3. Handling Exceptions with `try` and `except`

### 3.1. Basic `try`/`except`

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 3.2. Catching Multiple Exceptions

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
```

### 3.3. Catching Multiple Exceptions in One Block

```python
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
```

### 3.4. Catching Any Exception (Not Recommended)

```python
except Exception as e:
    print(f"An error occurred: {e}")
```

**Best Practice:** Catch specific exceptions rather than a broad `except`.

### 3.5. Accessing Exception Details

```python
try:
    x = int("abc")
except ValueError as e:
    print(f"Error details: {e}")   # invalid literal for int() with base 10: 'abc'
```

---

## 4. `else` and `finally` Clauses

### 4.1. `else` Clause

Executes if no exception was raised in the `try` block.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a number!")
else:
    print(f"Great! You entered {num}.")
```

### 4.2. `finally` Clause

Executes **always**, regardless of whether an exception occurred or not. Used for cleanup (closing files, releasing resources).

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file.")
    file.close()   # always executed
```

---

## 5. Raising Exceptions

Use `raise` to trigger an exception manually.

### 5.1. Raising Built‑in Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

### 5.2. Re‑raising an Exception

```python
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Logging error...")
    raise   # re‑raise the same exception
```

---

## 6. Creating Custom Exceptions

Custom exceptions are user‑defined classes that inherit from `Exception`.

```python
class NegativeNumberError(Exception):
    """Raised when a negative number is encountered."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of negative number")
    return x ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(e)
```

**Convention:** Name custom exceptions with “Error” suffix and inherit from `Exception` (or a more specific subclass).

---

## 7. Best Practices for Exception Handling

1. **Be specific:** Catch only exceptions you expect.
2. **Don’t silence exceptions:** Avoid empty `except:` blocks.
3. **Use `finally` for cleanup:** Close files, release resources.
4. **Log exceptions:** In real applications, log errors for debugging.
5. **Raise exceptions early:** Validate inputs and raise appropriate exceptions.
6. **Use custom exceptions for application‑specific errors.**

---

## 8. Hands‑On Activities

### Activity 1: Basic Input Validation

Write a program that asks the user for two numbers and divides them. Handle `ZeroDivisionError` and `ValueError`.

**Solution:**

```python
while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result = num1 / num2
        print(f"Result: {result}")
        break
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")
```

### Activity 2: File Reader with Exception Handling

Create a program that reads a file given by the user and prints its content. Handle `FileNotFoundError` and `PermissionError`. Use `finally` to close the file.

**Solution:**

```python
filename = input("Enter filename: ")
file = None
try:
    file = open(filename, "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    if file:
        file.close()
        print("File closed.")
```

### Activity 3: Raising Exceptions in a Function

Write a function `withdraw(amount, balance)` that raises a `ValueError` if `amount` exceeds `balance` or if `amount` is negative. Test with a `try/except` block.

**Solution:**

```python
def withdraw(amount, balance):
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative")
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    return balance

try:
    new_balance = withdraw(150, 100)
    print(f"New balance: {new_balance}")
except ValueError as e:
    print(f"Error: {e}")
```

### Activity 4: Custom Exception

Create a custom exception `InvalidAgeError`. Write a program that asks for age and raises the exception if age is not between 0 and 120.

**Solution:**

```python
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Age {age} is out of valid range (0-120)")
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age.")
except ValueError:
    print("Please enter a number.")
except InvalidAgeError as e:
    print(e)
```

### Activity 5: Calculator with Comprehensive Exception Handling

Build a simple calculator that asks for two numbers and an operator. Use exception handling to catch division by zero, invalid operator, and input conversion errors.

**Solution:**

```python
def calculator():
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        op = input("Operator (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError(f"Unsupported operator: {op}")

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Input error: {e}")
    except ZeroDivisionError as e:
        print(e)

calculator()
```

---

## 9. Common Pitfalls & Troubleshooting

| Problem                                          | Likely Cause                             | Solution                                               |
| ------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------ |
| `except:` without exception type                 | Catching everything, hiding bugs         | Always specify exception types                         |
| Using `except Exception` but missing subclasses  | Works, but may catch too much            | Still better than bare `except`, but be specific       |
| `finally` block raising another exception        | Overwrites original exception            | Avoid raising in `finally`; use `try` inside if needed |
| Not re‑raising after logging                     | Silencing error after log                | Use `raise` without arguments to preserve traceback    |
| Custom exception not inheriting from `Exception` | Will not be caught by `except Exception` | Always inherit from `Exception` or a subclass          |

---

## 10. Summary

- **Exceptions** are runtime errors that can be handled to prevent crashes.
- Use `try`/`except` to catch exceptions.
- `else` runs if no exception, `finally` runs regardless.
- Raise exceptions with `raise` to signal errors.
- Create **custom exceptions** by subclassing `Exception`.
- Follow best practices: be specific, clean up resources, and don’t silence errors.

---

## 11. Additional Resources

- [Python Official: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)
- [Python Exception Handling Best Practices](https://docs.python.org/3/howto/doanddont.html#exceptions)

---
