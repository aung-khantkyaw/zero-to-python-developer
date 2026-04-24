# Module 6: Modules and Packages

**Goal:** Learn how to structure Python projects, reuse code across files, and leverage the rich ecosystem of third‑party libraries.

## 1. What are Modules and Packages?

- **Module:** A single Python file (`.py`) that contains definitions (functions, classes, variables) and statements.
- **Package:** A directory containing multiple modules and an `__init__.py` file (can be empty). Packages allow hierarchical organization.

**Why use modules/packages?**

- Reusability: write once, use in multiple projects.
- Namespace management: avoid name collisions.
- Maintainability: split large codebases into manageable pieces.

---

## 2. Importing Modules

### 2.1. Basic Import

```python
import math

print(math.sqrt(16))   # 4.0
```

### 2.2. Import Specific Items

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0
print(pi)         # 3.1415...
```

### 2.3. Import with Alias

```python
import numpy as np   # common alias
from math import sqrt as square_root

print(square_root(9))   # 3.0
```

### 2.4. Import All (Not Recommended)

```python
from math import *   # pollutes namespace
```

**Avoid** – makes code harder to read and can cause name conflicts.

### 2.5. Importing Your Own Modules

If you have a file `mymodule.py` in the same directory:

```python
import mymodule

# or
from mymodule import some_function
```

---

## 3. The Python Standard Library

Python comes with a rich standard library. Here are some commonly used modules:

| Module | Description | Example |
| --- | --- | --- |
| `math` | Mathematical functions | `math.sin()`, `math.pi` |
| `random` | Generate random numbers | `random.randint(1,10)` |
| `datetime` | Date and time handling | `datetime.datetime.now()` |
| `os` | Operating system interface | `os.getcwd()`, `os.listdir()` |
| `sys` | System‑specific parameters | `sys.argv`, `sys.exit()` |
| `json` | JSON encoding/decoding | `json.loads()`, `json.dumps()` |
| `re` | Regular expressions | `re.search()`, `re.findall()` |
| `collections` | Advanced data structures | `defaultdict`, `Counter` |
| `pathlib` | Object‑oriented filesystem paths | `Path('file.txt').read_text()` |

**Example:**

```python
import random
import datetime

print(random.randint(1, 100))
print(datetime.datetime.now())
```

---

## 4. Creating Your Own Modules

### 4.1. Simple Module

Create a file `mymath.py`:

```python
# mymath.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

In another file (or interactive session):

```python
import mymath

print(mymath.add(5, 3))      # 8
print(mymath.multiply(4, 2)) # 8
print(mymath.PI)             # 3.14159
```

### 4.2. Module Search Path

Python looks for modules in:

1. The current directory.
2. Directories listed in `PYTHONPATH`.
3. Installation‑dependent default paths (e.g., `site-packages`).

You can view the search path with:

```python
import sys
print(sys.path)
```

---

## 5. The `if __name__ == "__main__"` Idiom

When a Python file is run directly, its `__name__` variable is set to `"__main__"`. When imported, `__name__` is set to the module's name. This idiom allows code to be executed only when the file is run directly, not when imported.

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This code runs only if executed directly
    print("Running as main script")
    print(greet("World"))
```

**Use case:** Write modules that can be both imported and executed as standalone scripts.

---

## 6. Packages

A package is a directory containing an `__init__.py` file (can be empty) and multiple module files.

### 6.1. Package Structure

```
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

### 6.2. Creating a Package

1. Create a directory (e.g., `shapes/`).
2. Add an empty `__init__.py`.
3. Add module files.

**Example:**

```
shapes/
    __init__.py
    circle.py
    rectangle.py
```

[**circle.py](http://circle.py/):**

```python
def area(radius):
    return 3.14159 * radius ** 2
```

[**rectangle.py](http://rectangle.py/):**

```python
def area(length, width):
    return length * width
```

### 6.3. Using the Package

```python
from shapes import circle, rectangle

print(circle.area(5))
print(rectangle.area(4, 6))
```

Or import inside `__init__.py` to expose functions directly.

---

## 7. Installing Third‑Party Packages with `pip`

`pip` is Python's package installer.

### 7.1. Basic Commands

```bash
# Install a package
pip install package_name

# Install a specific version
pip install package_name==1.2.3

# Upgrade a package
pip install --upgrade package_name

# Uninstall
pip uninstall package_name

# List installed packages
pip list

# Show package details
pip show package_name
```

### 7.2. Popular Third‑Party Packages

| Package | Purpose |
| --- | --- |
| `requests` | HTTP requests |
| `numpy` | Numerical computing |
| `pandas` | Data analysis |
| `matplotlib` | Plotting |
| `flask` | Web development |
| `django` | Full‑stack web framework |

**Example:**

```bash
pip install requests
```

```python
import requests

response = requests.get("<https://api.github.com>")
print(response.status_code)
```

---

## 8. Virtual Environments

Virtual environments isolate project dependencies, avoiding conflicts between projects.

### 8.1. Creating a Virtual Environment

```bash
# Using venv (built‑in)
python -m venv myenv

# Activate on Windows
myenv\\Scripts\\activate

# Activate on macOS/Linux
source myenv/bin/activate
```

### 8.2. Managing Dependencies

Once activated, install packages with `pip`. To export requirements:

```bash
pip freeze > requirements.txt
```

To install from a requirements file:

```bash
pip install -r requirements.txt
```

### 8.3. Deactivating

```bash
deactivate
```

**Best Practice:** Always use a virtual environment for projects.

---

## 9. Hands‑On Activities

### Activity 1: Explore the Standard Library

Write a program that:

- Generates a random number between 1 and 100.
- Gets the current date and time.
- Creates a directory named `test_dir` using `os` (or `pathlib`).

**Solution:**

```python
import random
import datetime
import os

print(random.randint(1, 100))
print(datetime.datetime.now())
os.mkdir("test_dir")
print("Directory created")
```

### Activity 2: Create and Use Your Own Module

1. Create a file `string_utils.py` with functions:
    - `reverse_string(s)` – returns reversed string.
    - `count_vowels(s)` – returns vowel count.
2. In another file, import and use these functions.

**Solution:**

```python
# string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# main.py
import string_utils

text = input("Enter a string: ")
print("Reversed:", string_utils.reverse_string(text))
print("Vowel count:", string_utils.count_vowels(text))
```

### Activity 3: Use `if __name__ == "__main__"` for Testing

Modify `string_utils.py` to include a test block that runs only when executed directly.

**Solution:**

```python
# string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    # Test the functions
    print(reverse_string("hello"))   # olleh
    print(count_vowels("Hello World"))  # 3
```

### Activity 4: Create a Simple Package

Create a package `geometry` with modules:

- `circle.py`: function `area(radius)`
- `rectangle.py`: function `area(length, width)`
- `triangle.py`: function `area(base, height)`

Then write a script that imports and uses them.

**Solution Structure:**

```
geometry/
    __init__.py
    circle.py
    rectangle.py
    triangle.py
```

[**circle.py](http://circle.py/):**

```python
import math
def area(radius):
    return math.pi * radius ** 2
```

[**rectangle.py](http://rectangle.py/):**

```python
def area(length, width):
    return length * width
```

[**triangle.py](http://triangle.py/):**

```python
def area(base, height):
    return 0.5 * base * height
```

[**main.py](http://main.py/):**

```python
from geometry import circle, rectangle, triangle

print(circle.area(5))
print(rectangle.area(4, 6))
print(triangle.area(3, 4))
```

### Activity 5: Install and Use an External Package

Install `requests` (if not installed) and write a program that fetches a URL and prints the status code and first 200 characters of the response.

**Solution:**

```python
import requests

url = input("Enter URL: ")
response = requests.get(url)
print(f"Status code: {response.status_code}")
print("First 200 chars:")
print(response.text[:200])
```

---

## 10. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| `ModuleNotFoundError` | Module not in search path or not installed | Check `pip list`, install if needed; verify file location |
| `ImportError: cannot import name` | Name misspelled or not defined in module | Check spelling and that the name exists |
| Package installed but still `ModuleNotFoundError` | Wrong Python environment | Ensure you're using the correct environment (activate virtual env) |
| `pip` not recognized | Python not added to PATH (Windows) | Reinstall Python with “Add to PATH” or use `python -m pip` |
| `__init__.py` missing in package | Python 3.3+ still needs it for namespace packages? Not required, but often used for initialization | Add empty `__init__.py` to make directory a regular package |

---

## 11. Summary

- **Modules** are `.py` files; **packages** are directories with `__init__.py`.
- Use `import`, `from ... import`, and aliases to bring code into your namespace.
- The standard library provides many useful modules.
- `if __name__ == "__main__"` allows code to run only when the file is executed directly.
- `pip` is the package manager for installing third‑party libraries.
- **Virtual environments** isolate project dependencies.
- Organize code into modules and packages to keep projects clean and reusable.

---

## 12. Additional Resources

- [Python Official: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Real Python: Python Modules and Packages](https://realpython.com/python-modules-packages/)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments (venv)](https://docs.python.org/3/library/venv.html)

---