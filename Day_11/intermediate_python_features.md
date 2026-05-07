# Module 10: Intermediate Python Features

**Goal:** Master advanced Python features that make code more concise, expressive, and efficient.

## 1. Comprehensions

Comprehensions provide a compact way to create collections from existing iterables.

### 1.1. List Comprehensions

```python
# Basic: [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]          # [0,1,4,9,16,25,36,49,64,81]
evens = [x for x in range(20) if x % 2 == 0] # [0,2,4,...,18]
```

### 1.2. Dictionary Comprehensions

```python
# {key_expression: value_expression for item in iterable}
squares_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### 1.3. Set Comprehensions

```python
# {expression for item in iterable}
unique_lengths = {len(word) for word in ["apple", "banana", "cherry"]} # {5,6}
```

### 1.4. Nested Comprehensions

```python
# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]  # [1,2,3,4,5,6]
```

---

## 2. Generator Expressions

Generator expressions are similar to list comprehensions but return an iterator that yields values lazily (one at a time), saving memory.

```python
# Generator expression (parentheses, not brackets)
gen = (x**2 for x in range(10))   # returns generator object

# Iterate (values computed on demand)
for value in gen:
    print(value)   # prints 0,1,4,... but not stored in memory all at once
```

**Use case:** Large datasets where you don’t need the entire list in memory.

**Conversion:** `list(gen)` if you need all values at once.

---

## 3. `args` and `*kwargs`

These allow functions to accept a variable number of arguments.

### 3.1. `args` (Variable Positional Arguments)

Collects extra positional arguments into a tuple.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 10
```

### 3.2. `*kwargs` (Variable Keyword Arguments)

Collects extra keyword arguments into a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```

### 3.3. Unpacking in Function Calls

Use `*` and `**` to unpack iterables/dictionaries into function arguments.

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))   # 6

kwargs = {'a': 1, 'b': 2, 'c': 3}
print(add(**kwargs))   # 6
```

---

## 4. Map, Filter, Reduce

These functional programming tools operate on iterables.

### 4.1. `map(function, iterable, ...)`

Applies function to every item and returns an iterator.

```python
nums = [1, 2, 3, 4]
squared = map(lambda x: x**2, nums)
print(list(squared))   # [1, 4, 9, 16]
```

### 4.2. `filter(function, iterable)`

Returns an iterator with items where function returns `True`.

```python
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))   # [2, 4]
```

### 4.3. `reduce(function, iterable[, initializer])`

Reduces the iterable to a single value by applying function cumulatively (from `functools`).

```python
from functools import reduce

product = reduce(lambda x, y: x * y, nums)   # 1*2*3*4 = 24
print(product)

# With initializer
product = reduce(lambda x, y: x * y, nums, 10)   # 10 * 1 * 2 * 3 * 4 = 240
```

**Comparison with comprehensions:** Comprehensions are often more readable. Use `map`/`filter` when you already have a named function or prefer functional style.

---

## 5. Decorators

Decorators are functions that modify the behavior of other functions without changing their source code.

### 5.1. Simple Decorator

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(delay):
    time.sleep(delay)
    return "Done"

print(slow_function(2))
```

### 5.2. Decorator with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))   # ['Hello, Alice', 'Hello, Alice', 'Hello, Alice']
```

### 5.3. Preserving Metadata with `functools.wraps`

Always use `@wraps` to copy metadata from the original function to the wrapper.

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper
```

---

## 6. Custom Context Managers

Context managers allow you to allocate and release resources precisely (like files, locks). Use the `with` statement.

### 6.1. Using Class with `__enter__` and `__exit__`

```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exception, False to propagate
        return False

with ManagedFile("hello.txt", "w") as f:
    f.write("Hello, world!")
```

### 6.2. Using `contextlib.contextmanager` (Generator‑Based)

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("hello.txt", "w") as f:
    f.write("Hello, world!")
```

---

## 7. Hands‑On Activities

### Activity 1: Comprehensions

1. Create a list of squares of even numbers from 0 to 20.
2. Create a dictionary mapping numbers to their cubes for numbers 1–10.
3. Create a set of all unique characters in the string `"abracadabra"`.

**Solution:**

```python
# 1
even_squares = [x**2 for x in range(0, 21, 2)]
# 2
cubes_dict = {x: x**3 for x in range(1, 11)}
# 3
unique_chars = {ch for ch in "abracadabra"}
```

### Activity 2: Generator Expression

Write a generator expression that yields the first 10 Fibonacci numbers. Use it to print them without storing all at once.

**Solution:**

```python
def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generator expression alternative (though not typical for Fibonacci)
# This is a simple demonstration:
fib_gen = (fib for fib in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  # hardcoded
# Better: define generator function and iterate
for val in fib_generator(10):
    print(val)
```

### Activity 3: Flexible Function with `args` and `*kwargs`

Write a function `create_person` that accepts:

- `args` – any number of strings (names)
- `*kwargs` – any number of attributes (e.g., age, city)
It should print each name and then the attributes.

**Solution:**

```python
def create_person(*args, **kwargs):
    print("Names:", args)
    print("Attributes:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_person("Alice", "Bob", age=25, city="NYC")
```

### Activity 4: Map, Filter, Reduce

Given a list of numbers, use:

- `map` to square them.
- `filter` to keep only those > 10.
- `reduce` to find the product of the remaining numbers.

**Solution:**

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x > 10, squared))
product = reduce(lambda x, y: x * y, filtered)
print(product)
```

### Activity 5: Decorator for Logging

Write a decorator `log` that prints the function name and arguments before calling the function. Apply it to a few functions.

**Solution:**

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("Alice", greeting="Hi")
```

### Activity 6: Custom Context Manager

Create a context manager `Timer` that measures how long a block of code takes. Use it with `with`.

**Solution (class‑based):**

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.4f} seconds")

with Timer():
    time.sleep(2)
```

**Solution (generator‑based):**

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed: {end - start:.4f} seconds")

with timer():
    time.sleep(2)
```

---

## 8. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| List comprehension uses too much memory | Storing large intermediate list | Use generator expression instead |
| `*args` / `**kwargs` order in function definition | Must be placed after positional parameters | Order: `def func(a, b, *args, **kwargs)` |
| Forgetting to unpack with `*` in call | Passing a list as a single argument | Use `*list` to unpack |
| `map` returns iterator, not list | Python 3 behavior | Wrap with `list()` if needed |
| Decorator loses original function metadata | Not using `@wraps` | Always import and use `functools.wraps` |
| Context manager doesn't close resource on exception | Forgetting to handle in `__exit__` | Ensure `__exit__` closes/cleans up; use `try/finally` in generator version |
| `reduce` not imported | It's in `functools` | `from functools import reduce` |

---

## 9. Summary

- **Comprehensions** provide concise ways to build lists, dicts, and sets.
- **Generator expressions** are memory‑efficient for large data.
- **`args` and `*kwargs`** allow functions to accept variable arguments.
- **`map`, `filter`, `reduce`** enable functional programming styles.
- **Decorators** modify function behavior elegantly.
- **Custom context managers** give fine‑grained resource control.

---

## 10. Additional Resources

- [Python Official: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python: Python Generators](https://realpython.com/introduction-to-python-generators/)
- [Python Official: `args` and `*kwargs`](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Real Python: Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python `contextlib` Documentation](https://docs.python.org/3/library/contextlib.html)

---