# Module 2: Python Basics

**Goal:** Understand Python’s fundamental building blocks: variables, data types, basic operations, and string manipulation.

## 1. Variables and Data Types

### 1.1. What is a Variable?

A variable is a named container for storing data. In Python, you don’t need to declare the type; it is inferred from the value.

```python
name = "Alice"     # string
age = 25           # integer
height = 1.75      # float
is_student = True  # boolean
```

**Rules for variable names:**

- Can contain letters, digits, and underscores.
- Must start with a letter or underscore (not a digit).
- Case‑sensitive (`name` ≠ `Name`).
- Cannot use Python keywords (e.g., `if`, `for`, `while`).

### 1.2. Data Types Overview

| Category | Type | Example | Description |
| --- | --- | --- | --- |
| **Text Type** | `str` | `"Hello"`, `'Python'`, `"""Multi-line"""` | Unicode string (text) |
| **Numeric Types** | `int` | `42`, `-5`, `0`, `1_000_000` | Integer (arbitrary precision) |
|  | `float` | `3.14`, `-0.001`, `1.2e3` | Double‑precision floating point |
|  | `complex` | `3+4j`, `-2j`, `1+0j` | Complex number (real + imaginary part) |
| **Sequence Types** | `list` | `[1, 2, 3]`, `['a', 'b']` | Mutable ordered collection |
|  | `tuple` | `(1, 2, 3)`, `('x', 'y')` | Immutable ordered collection |
|  | `range` | `range(5)`, `range(1,10,2)` | Immutable sequence of numbers (used in loops) |
| **Mapping Type** | `dict` | `{'name': 'Alice', 'age': 25}` | Key‑value pairs (associative array) |
| **Set Types** | `set` | `{1, 2, 3}`, `set([1,2,2])` | Unordered collection of unique, mutable items |
|  | `frozenset` | `frozenset([1,2,3])` | Immutable version of a set |
| **Boolean Type** | `bool` | `True`, `False` | Logical values (subclass of `int`) |
| **Binary Types** | `bytes` | `b'hello'`, `bytes([65,66])` | Immutable sequence of bytes (0–255) |
|  | `bytearray` | `bytearray([65,66])` | Mutable sequence of bytes |
|  | `memoryview` | `memoryview(b'hello')` | Memory‑view of binary data (no copy) |
| **None Type** | `NoneType` | `None` | Represents absence of a value (only one instance: `None`) |

---

### Quick Examples

```python
# Numeric types
x = 3 + 4j          # complex
print(x.real, x.imag)  # 3.0 4.0

# Sequence types
r = range(3)        # 0,1,2
print(list(r))      # [0, 1, 2]

# Set types
fs = frozenset([1,2,2])
print(fs)           # frozenset({1,2})

# Binary types
b = bytes([65,66,67])   # b'ABC'
ba = bytearray(b'hello')
ba[0] = 72          # modify to b'Hello'
print(ba)           # bytearray(b'Hello')

# NoneType
value = None
print(type(value))  # <class 'NoneType'>
```

You can check the type of any variable using `type()`:

```python
print(type(age))   # <class 'int'>
```

---

## 2. Basic Operations

### 2.1. Arithmetic Operators

| Operator | Description | Example |
| --- | --- | --- |
| `+` | Addition | `5 + 3 → 8` |
| `-` | Subtraction | `5 - 3 → 2` |
| `*` | Multiplication | `5 * 3 → 15` |
| `/` | Division (float) | `5 / 2 → 2.5` |
| `//` | Floor division | `5 // 2 → 2` |
| `%` | Modulo (remainder) | `5 % 2 → 1` |
| `**` | Exponentiation | `5 ** 2 → 25` |

**Order of operations:** Python follows PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction).

### 2.2. Comparison Operators

| Operator | Description | Example |
| --- | --- | --- |
| `==` | Equal to | `5 == 5 → True` |
| `!=` | Not equal to | `5 != 3 → True` |
| `>` | Greater than | `5 > 3 → True` |
| `<` | Less than | `5 < 3 → False` |
| `>=` | Greater than or equal | `5 >= 5 → True` |
| `<=` | Less than or equal | `5 <= 3 → False` |

### 2.3. Logical Operators

| Operator | Description | Example |
| --- | --- | --- |
| `and` | True if both are true | `(5 > 3) and (2 < 4) → True` |
| `or` | True if at least one is true | `(5 > 3) or (2 > 4) → True` |
| `not` | Reverses the boolean | `not (5 > 3) → False` |

---

## 3. Type Conversion (Casting)

Sometimes you need to convert a value from one type to another.

```python
# Convert string to int
num_str = "123"
num_int = int(num_str)

# Convert int to float
num_float = float(10)   # 10.0

# Convert float to int (truncates)
num_int = int(3.99)     # 3

# Convert number to string
text = str(42)          # "42"

# Convert to boolean
bool(0)      # False
bool(1)      # True
bool("")     # False
bool("Hi")   # True
```

> **Note:** `input()` always returns a string. Use casting to treat input as numbers:
> 
> 
> ```python
> age = int(input("Enter your age: "))
> ```
> 

---

## 4. Strings in Depth

Strings are sequences of characters. They can be enclosed in single, double, or triple quotes.

### 4.1. Indexing and Slicing

Each character has an index (starting from 0). Negative indices count from the end.

```python
text = "Python"
# Indices:  P  y  t  h  o  n
#          0  1  2  3  4  5
#         -6 -5 -4 -3 -2 -1

# Access single character
print(text[0])   # 'P'
print(text[-1])  # 'n'

# Slicing: [start:stop:step]
print(text[0:3])   # 'Pyt' (stop index excluded)
print(text[2:])    # 'thon' (from index 2 to end)
print(text[:4])    # 'Pyth' (from start to index 3)
print(text[::2])   # 'Pto' (every 2nd character)
print(text[::-1])  # 'nohtyP' (reverse)
```

### 4.2. Common String Methods

| Method | Description | Example |
| --- | --- | --- |
| `upper()` | Returns uppercase version | `"hello".upper() → "HELLO"` |
| `lower()` | Returns lowercase version | `"HELLO".lower() → "hello"` |
| `strip()` | Removes leading/trailing whitespace | `"  hi  ".strip() → "hi"` |
| `replace(old, new)` | Replaces substring | `"hello".replace("l", "x") → "hexxo"` |
| `split(sep)` | Splits into list | `"a,b,c".split(",") → ["a","b","c"]` |
| `join(iterable)` | Joins elements with string | `"-".join(["a","b","c"]) → "a-b-c"` |
| `find(sub)` | Returns index of first occurrence | `"hello".find("l") → 2` |
| `count(sub)` | Counts occurrences | `"hello".count("l") → 2` |
| `startswith(prefix)` | Checks if starts with | `"hello".startswith("he") → True` |
| `endswith(suffix)` | Checks if ends with | `"hello".endswith("lo") → True` |

**Examples:**

```python
text = "  Hello, World!  "
print(text.strip())           # "Hello, World!"
print(text.lower())           # "  hello, world!  "
print(text.replace("World", "Python"))  # "  Hello, Python!  "
print("apple,banana,cherry".split(",")) # ['apple', 'banana', 'cherry']
```

---

## 5. Hands‑On Activities

### Activity 1: Variable Practice

Create variables for your favorite movie (string), its release year (int), rating (float), and whether you’ve watched it (bool). Print each variable with a label.

**Solution:**

```python
movie = "Inception"
year = 2010
rating = 8.8
watched = True

print("Movie:", movie)
print("Year:", year)
print("Rating:", rating)
print("Watched:", watched)
```

### Activity 2: Simple Calculator with User Input

Write a program that asks the user for two numbers and displays the sum, difference, product, quotient, and floor division.

**Solution:**

```python
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Floor division: {num1 // num2}")
```

### Activity 3: Comparison and Logic

Write a program that asks for the user’s age and prints:

- `"Adult"` if age ≥ 18
- `"Minor"` if age < 18
- Also print `"Eligible to vote"` if age ≥ 18 and the user is a citizen (ask a boolean question).

**Solution:**

```python
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower() == "yes"

if age >= 18:
    print("Adult")
    if citizen:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Minor")
```

### Activity 4: String Manipulation

Given the string: `"   Python programming is fun!   "`

1. Remove extra spaces.
2. Convert to uppercase.
3. Replace `"fun"` with `"awesome"`.
4. Split into words and print the first three words.

**Solution:**

```python
s = "   Python programming is fun!   "
s = s.strip()
s = s.upper()
s = s.replace("FUN", "AWESOME")
words = s.split()
print(words[:3])
```

---

## 6. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| `TypeError: unsupported operand type(s)` | Mixing incompatible types (e.g., `"5" + 3`) | Cast to appropriate type, e.g., `int("5") + 3` |
| `ValueError: invalid literal for int()` | `int()` called on a non‑numeric string | Validate input or use `try/except` (later) |
| String index out of range | Accessing index beyond string length | Check length with `len()` before indexing |
| Unexpected results with `/` vs `//` | Confusing division types | Remember `/` always returns float, `//` floors |
| `input()` returns string for numbers | Forgetting to cast | Use `int(input())` or `float(input())` |

---

## 7. Summary

- Variables store data; Python infers types dynamically.
- Basic types: `int`, `float`, `str`, `bool`.
- Use arithmetic, comparison, and logical operators to manipulate data.
- Cast between types when necessary, especially when reading user input.
- Strings are sequences – use indexing, slicing, and methods for powerful text processing.
- f‑strings provide a clean way to embed variables in strings.

---

## 8. Additional Resources

- [Python Data Types (Official)](https://docs.python.org/3/library/stdtypes.html)
- [String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [W3Schools Python Strings](https://www.w3schools.com/python/python_strings.asp)
- [Real Python: Basic Data Types](https://realpython.com/python-data-types/)

---