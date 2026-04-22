# Module 5: Functions

**Goal:** Learn how to write reusable, modular code using functions, understand scope, and explore functional programming basics.

## 1. What is a Function?

A function is a reusable block of code that performs a specific task. Functions help:

- **Avoid repetition** (DRY – Don’t Repeat Yourself)
- **Organize code** into logical sections
- **Make testing easier** by isolating functionality

### 1.1. Defining a Function

```python
def function_name(parameters):
    """Optional docstring"""
    # function body
    return value   # optional
```

**Example:**

```python
def greet():
    print("Hello, World!")

greet()   # call the function
```

### 1.2. Parameters and Arguments

- **Parameters** are variables listed in the function definition.
- **Arguments** are values passed when calling the function.

```python
def greet(name):          # name is a parameter
    print(f"Hello, {name}!")

greet("Alice")            # "Alice" is an argument
```

---

## 2. Types of Arguments

### 2.1. Positional Arguments

Arguments are passed in the same order as parameters.

```python
def add(a, b):
    return a + b

result = add(3, 5)   # a=3, b=5
```

### 2.2. Keyword Arguments

Arguments are passed by parameter name, order doesn’t matter.

```python
result = add(b=5, a=3)
```

### 2.3. Default Parameters

Assign a default value to a parameter. If omitted, the default is used.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")               # Hello, Alice!
greet("Bob", "Hi")           # Hi, Bob!
```

**Important:** Default parameters must come after non‑default parameters.

### 2.4. Variable‑Length Arguments

- `args` – accepts any number of positional arguments (as a tuple)
- `*kwargs` – accepts any number of keyword arguments (as a dictionary)

```python
def print_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

print_args(1, 2, 3, name="Alice", age=25)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'age': 25}
```

---

## 3. Return Values

A function can return a value using the `return` statement. If no `return`, the function returns `None`.

```python
def add(a, b):
    return a + b

result = add(4, 6)
print(result)   # 10

def no_return():
    print("This returns None")

value = no_return()
print(value)    # None
```

### 3.1. Returning Multiple Values

Return a tuple; unpack at call time.

```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([4, 2, 9, 1])
print(minimum, maximum)   # 1 9
```

---

## 4. Scope of Variables

**Scope** determines where a variable can be accessed.

### 4.1. Local Scope

Variables defined inside a function are local to that function.

```python
def my_func():
    x = 10      # local variable
    print(x)

my_func()
# print(x)   # NameError: x is not defined
```

### 4.2. Global Scope

Variables defined outside any function are global. Use the `global` keyword to modify them inside a function.

```python
count = 0   # global

def increment():
    global count
    count += 1

increment()
print(count)   # 1
```

**Best Practice:** Avoid modifying globals; use parameters and return values instead.

### 4.3. `nonlocal` for Nested Functions

`nonlocal` allows modifying variables in the outer (enclosing) scope.

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)   # 15
```

---

## 5. Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword.

```python
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))   # 25

# Often used with map, filter, sort
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))   # [1,4,9,16]
evens = list(filter(lambda x: x % 2 == 0, numbers))   # [2,4]
```

---

## 6. Docstrings

Docstrings (documentation strings) describe what a function does. They are written as the first statement in a function body.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(help(add))   # Shows the docstring
print(add.__doc__) # Access directly
```

**Convention:** Use triple‑quoted strings and follow PEP 257.

---

## 7. Recursion (Optional)

Recursion is a function calling itself. It must have a base case to stop.

```python
def factorial(n):
    """Return n! (n factorial) using recursion."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))   # 120
```

**When to use:** Problems that can be broken into similar sub‑problems (tree traversal, divide‑and‑conquer). **Caution:** Python has recursion limit (~1000).

---

## 8. Hands‑On Activities

### Activity 1: Simple Calculator Functions

Create functions for addition, subtraction, multiplication, and division. Then write a main program that asks the user for two numbers and an operation, and calls the appropriate function.

**Solution:**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Main program
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == '+':
    print(add(num1, num2))
elif op == '-':
    print(subtract(num1, num2))
elif op == '*':
    print(multiply(num1, num2))
elif op == '/':
    print(divide(num1, num2))
else:
    print("Invalid operation")
```

### Activity 2: Greeting with Default Parameter

Write a function `greet(name, greeting="Hello")` that prints a greeting. Test it with and without the greeting argument.

**Solution:**

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
```

### Activity 3: Variable‑Length Arguments Sum

Write a function `sum_all(*args)` that returns the sum of all numbers passed.

**Solution:**

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 10
print(sum_all(5, 10))        # 15
```

### Activity 4: Palindrome Check

Write a function `is_palindrome(s)` that returns `True` if the string is a palindrome (ignoring case and spaces). Use it in a main program.

**Solution:**

```python
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
```

### Activity 5: Recursive Fibonacci

Write a recursive function `fibonacci(n)` that returns the nth Fibonacci number (0, 1, 1, 2, 3, 5, ...). Test with n=10.

**Solution:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))   # 55
```

**Note:** Discuss performance; iterative version is more efficient.

---

## 9. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| `NameError: name 'x' is not defined` | Trying to use a local variable outside its function | Return the value and assign to a variable in the caller |
| `TypeError: missing 1 required positional argument` | Not enough arguments passed | Check function signature; provide default values if appropriate |
| Modifying global variable unintentionally | Forgetting `global` inside function | Use `global` if needed, but better to pass as parameter and return |
| Mutable default arguments | Using a mutable object (e.g., list) as default; changes persist | Use `None` as default and create new object inside |
| `RecursionError: maximum recursion depth exceeded` | Missing base case or too deep recursion | Add base case; consider iterative alternative |

---

## 10. Summary

- **Functions** encapsulate reusable code.
- Use parameters to pass data; return values to send data back.
- **Argument types:** positional, keyword, default, `args`, `*kwargs`.
- **Scope:** local variables exist only inside function; global variables need `global` to modify.
- **Lambda functions** are anonymous, short functions.
- **Docstrings** document your code.
- **Recursion** is a function calling itself; must have a base case.

---

## 11. Additional Resources

- [Python Official: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
- [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Python Scope & LEGB Rule](https://realpython.com/python-scope-legb-rule/)

---