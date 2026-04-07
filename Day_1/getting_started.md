# Module 1: Getting Started

**Goal:** Set up the Python environment, write the first program, understand basic syntax, and get comfortable with the development workflow.

## 1. What is Python?

**Python** is a high‑level, general‑purpose programming language widely recognized for:

- **Simplicity** – Clean and intuitive syntax that feels almost like plain English.
- **Readability** – Code is easy to understand and maintain, even for large projects.
- **Versatility** – Applicable across many domains, from web development to artificial intelligence.
- **Large ecosystem** – Thousands of libraries available via `pip`.
- **Beginner‑friendly** – Gentle learning curve, making it an ideal first language.

**Key Milestones:**

| Milestone | Detail |
| --- | --- |
| **Creator** | Guido van Rossum |
| **Initial Release** | 1991 |
| **Philosophy** | “Readability matters” – [PEP 20 (The Zen of Python)](https://peps.python.org/pep-0020/) |

**Primary Application Areas:**

| Area | Examples |
| --- | --- |
| **Data Science & Artificial Intelligence** | NumPy, pandas, TensorFlow, PyTorch, scikit‑learn |
| **Web Development** | Django, Flask, FastAPI |
| **Process Automation & Scripting** | Task automation, system administration, web scraping |
| **Software Testing** | pytest, Selenium, unittest, behave |
| **Other domains** | DevOps (Ansible), Game development (Pygame), Desktop GUI (Tkinter, PyQt) |

**Example:**

```python
print("Hello, World!")
```

> *“Python is an experiment in how much freedom programmers need. Too much freedom lets a program be written in incomprehensible ways; too little freedom makes solutions cumbersome. Python strikes a balance.”*
> 
> 
> – Guido van Rossum
> 

---

## 2. Installing Python

### 2.1. Check if Python is already installed

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and type:

```bash
python --version
```

or

```bash
python3 --version
```

If you see a version number (e.g., `Python 3.12.0`), you already have Python.

### 2.2. Download and install

- Go to [python.org/downloads](https://www.python.org/downloads/)
- Download the latest stable version (3.x)
- **Windows**: During installation, **check the box** “Add Python to PATH” – this is crucial.
- **macOS/Linux**: Use the official installer or package manager (e.g., `brew install python` on macOS, `sudo apt install python3` on Linux).

**After installation**, verify again:

```bash
python --version
```

---

## 3. Setting Up a Code Editor

Python can be run from the terminal, but a good editor improves productivity.

### 3.1. Recommended options

| Editor | Pros | When to use |
| --- | --- | --- |
| **VS Code** | Free, lightweight, excellent Python extension | Most versatile, recommended for beginners |
| **PyCharm** | Powerful IDE, built‑in tools | Great for larger projects |
| **IDLE** | Comes with Python, very simple | Quick tests, no installation needed |

### 3.2. Installing VS Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the **Python extension** by Microsoft
3. Open a folder for your Python projects.

### 3.3. Installing PyCharm

1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm).
2. Run installer → choose Community (free) or Professional.
3. Launch PyCharm → **New Project** → select Python interpreter.
4. Click **Create**.

---

## 4. Running Python Code

### 4.1. Interactive Mode (REPL)

Type `python` (or `python3`) in the terminal. You’ll see `>>>`. You can write Python commands and see immediate results.

```python
>>> print("Hi")
Hi
>>> 2 + 3
5
>>> exit()   # or Ctrl+Z on Windows, Ctrl+D on macOS/Linux
```

Useful for quick experiments.

### 4.2. Script Mode (File)

Create a file named `hello.py` with the following content:

```python
print("Hello, World!")
```

Then run it from the terminal:

```bash
python hello.py
```

Or use the “Run” button in your editor.

---

## 5. Your First Python Program: `print()` and `input()`

### 5.1. The `print()` function

Displays output to the console.

```python
print("Hello")
print(42)
print("The result is", 5 + 3)
```

- Multiple items can be separated by commas.
- By default, `print()` adds a newline at the end.

### 5.2. The `input()` function

Reads a line of text from the user and returns it as a string.

```python
name = input("What is your name? ")
print("Hello", name)
```

- The argument is the prompt shown to the user.
- 1The returned value is always a string; convert it if needed (e.g., `int(input("..."))`).

### 5.3. Simple program combining both

```python
# Ask for user's name and age
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name, "! You are", age, "years old.")
```

### **5.4. String Formatting: `format()` and f‑strings**

String formatting lets you insert values into a string. Python provides two common ways: the `format()` method and **f‑strings** (formatted string literals).

### **A. The `format()` method**

The `format()` method uses `{}` as placeholders.

```python
name = "Alice"
age = 25
print("Hello, {}. You are {} years old.".format(name, age))
```

- Values are inserted in order.
- You can change the order with numbered placeholders:

```python
print("My name is {1}. I am {0} years old.".format(age, name))
# Output: My name is Alice. I am 25 years old.
```

- You can use named placeholders for clarity:

```python
print("Hello, {n}. You are {a} years old.".format(n=name, a=age))
```

**Why use `format()`?**

- Works in all Python versions (even older ones before 3.6).
- Allows dynamic formatting strings (e.g., templates read from a file).
- Gives fine control over spacing, alignment, and number formatting (e.g., `"{:.2f}".format(3.14159)` → `"3.14"`).

### **B. f‑strings (Formatted String Literals) – Python 3.6+**

f‑strings are a newer, more concise way to format strings. Put an `f` before the string and use `{variable}` directly.

```python
name = "Alice"
age = 25
print(f"Hello, {name}. You are {age} years old.")
```

- You can put expressions inside `{}`:

```python
print(f"5 + 3 = {5 + 3}")
```

- You can call methods:

```python
print(f"Uppercase: {name.upper()}")
```

- You can format numbers:

```python
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")   # Pi to 2 decimals: 3.14
```

**Why use f‑strings?**

- Cleaner and easier to read.
- Faster than `format()` because it is evaluated at compile time.

### **C. Comparison Table**

| Feature | `format()` | f‑string |
| --- | --- | --- |
| **Introduced** | Python 2.6 / 3.0 | Python 3.6 |
| **Syntax** | `"Hello {}".format(name)` | `f"Hello {name}"` |
| **Readability** | Good | Excellent |
| **Performance** | Slower | Faster |
| **Dynamic template** | Yes (from variable) | No (must be literal) |
| **Expression inside** | Limited | Full Python expressions |

### **D. Which one should you use?**

| Situation | Recommendation |
| --- | --- |
| **You are using Python 3.6+** | Prefer **f‑strings** – they are simpler and faster. |
| **You need a dynamic template** (e.g., from a file or user input) | Use **`format()`** because f‑strings require a literal string. |
| **You must support old Python (before 3.6)** | Use **`format()`** or the older `%` formatting. |

### **E. Examples side‑by‑side**

```python
name = "Bob"
score = 95.678

# f-string (modern)
print(f"{name} scored {score:.1f} points.")

# format() method
print("{} scored {:.1f} points.".format(name, score))

# Both output: Bob scored 95.7 points.
```

---

## 6. Comments and Code Readability

Comments are ignored by Python but help humans understand the code.

- **Single‑line comment**: start with `#`

```python
# This is a comment
print("Hello")   # This is an inline comment
```

- **Multi‑line comment**: use triple quotes (often for docstrings)

```python
"""
This is a
multi-line comment
"""
```

**Best practices:**

- Use comments to explain *why*, not *what* (the code should be self‑explanatory).
- Keep comments up‑to‑date.
- Use meaningful variable names.

---

## 7. Hands‑On Activities

### Activity 1: Environment Check

1. Verify Python installation.
2. Run the Python interpreter and type `print("Python is working!")`.
3. Exit the interpreter and run the same command from a script file.

### Activity 2: Personal Greeting

Write a program that:

- Asks the user for their first name and last name.
- Prints a greeting like: “Hello, John Doe!”

**Solution:**

```python
first = input("First name: ")
last = input("Last name: ")
print("Hello,", first, last, "!")
```

### Activity 3: Simple Calculator (with integers)

Write a program that asks for two numbers and prints their sum, difference, product, and quotient.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
```

### Activity 4: Comment Your Code

Take the calculator program and add comments explaining each step.

---

## 8. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| `python` not recognized | Python not added to PATH (Windows) | Reinstall Python and check “Add to PATH” |
| `SyntaxError: invalid syntax` | Typo, missing quotes, wrong indentation | Check line carefully, ensure quotes match |
| `NameError: name '...' is not defined` | Variable used before assignment or misspelled | Verify spelling and order |
| `input()` returns a string but you need a number | Forgot to convert with `int()` or `float()` | Use `int(input(...))` |

---

## 9. Summary

- Python is a versatile, beginner‑friendly language.
- Install Python and a code editor to start coding.
- Run Python in interactive mode for tests, and script mode for programs.
- `print()` displays output, `input()` reads user input.
- Comments improve code readability.

---

## 10. Additional Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python.org Beginner’s Guide](https://www.python.org/about/gettingstarted/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

---