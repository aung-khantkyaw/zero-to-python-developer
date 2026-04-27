# Module 7: File Handling

**Goal:** Learn how to read from and write to files, manage file paths, and work with structured data formats (CSV, JSON).

## 1. Why File Handling?

File handling allows programs to:

- Persist data beyond program execution.
- Process large datasets stored in files.
- Interact with configuration files, logs, and user data.
- Exchange data with other applications using standard formats (CSV, JSON).

---

## 2. Working with Text Files

### 2.1. Opening a File

Use `open(filename, mode)` to return a file object.

**Common modes:**

| Mode | Description |
| --- | --- |
| `'r'` | Read (default). File must exist. |
| `'w'` | Write. Creates new file or overwrites existing. |
| `'a'` | Append. Adds to end of file. |
| `'r+'` | Read and write. |
| `'x'` | Exclusive creation. Fails if file exists. |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`). |

**Example:**

```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

### 2.2. Reading Files

```python
with open("example.txt", "r") as file:
    entire = file.read()
    print(entire)
```

### 2.3. Writing Files

```python
with open("output.txt", "w") as file:
    file.write("Hello, world!\\n")
    file.write("Second line\\n")
```

### 2.4. Appending to Files

```python
with open("output.txt", "a") as file:
    file.write("Appended line\\n")
```

### 2.5. The `with` Statement (Context Manager)

Using `with` ensures the file is properly closed even if an error occurs.

```python
with open("data.txt", "r") as f:
    data = f.read()
# File is automatically closed
```

**Alternative:** Without `with`, you must manually close:

```python
f = open("data.txt", "r")
data = f.read()
f.close()
```

**Recommendation:** Always use `with`.

---

## 3. Working with File Paths

### 3.1. Using `os.path` (Legacy)

```python
import os

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")

# Check existence
if os.path.exists(path):
    print("File exists")

# Get absolute path
abs_path = os.path.abspath("file.txt")

# Get directory and filename
dirname = os.path.dirname(path)
basename = os.path.basename(path)

# Split extension
name, ext = os.path.splitext("file.txt")   # ('file', '.txt')
```

### 3.2. Using `pathlib` (Modern, Recommended)

`pathlib` provides an object‑oriented approach.

```python
from pathlib import Path

# Create a Path object
path = Path("folder") / "subfolder" / "file.txt"

# Check existence
if path.exists():
    print("Exists")

# Read/write files easily
content = path.read_text()
path.write_text("New content")

# Get absolute path
abs_path = path.absolute()

# Get parts
print(path.parent)      # folder/subfolder
print(path.name)        # file.txt
print(path.stem)        # file
print(path.suffix)      # .txt
```

**Advantages:** Cross‑platform, more readable, chainable methods.

---

## 4. Working with CSV Files

CSV (Comma‑Separated Values) is a common data exchange format.

### 4.1. Reading CSV Files

```python
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row is a list of strings
```

If the file has a header row, you can use `DictReader` for dictionary access:

```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)   # first row becomes keys
    for row in reader:
        print(row["Name"], row["Age"])
```

### 4.2. Writing CSV Files

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"]
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

For dictionaries:

```python
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"}
]

with open("output.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

**Note:** Use `newline=""` to avoid extra blank lines on Windows.

---

## 5. Working with JSON Files

JSON (JavaScript Object Notation) is widely used for data interchange.

### 5.1. Reading JSON

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)   # parses JSON into Python dict/list
print(data["name"])
```

### 5.2. Writing JSON

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)   # indent for pretty formatting
```

### 5.3. Working with JSON Strings

```python
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)          # string to Python object
output_string = json.dumps(data)        # Python object to JSON string
```

---

## 6. Handling File‑Related Exceptions

Common exceptions:

- `FileNotFoundError`: file does not exist (when reading).
- `PermissionError`: insufficient permissions.
- `IsADirectoryError`: expected a file but got a directory.

Use `try/except` to handle gracefully:

```python
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
```

---

## 7. Hands‑On Activities

### Activity 1: Create and Read a Text File

Write a program that:

1. Asks the user for a filename and some lines of text (stop on empty input).
2. Writes those lines to the file.
3. Reads and displays the file content.

**Solution:**

```python
filename = input("Enter filename: ")

# Write
with open(filename, "w") as f:
    print("Enter lines (empty line to stop):")
    while True:
        line = input()
        if not line:
            break
        f.write(line + "\\n")

# Read
with open(filename, "r") as f:
    print("\\nFile content:")
    print(f.read())
```

### Activity 2: File Copy

Write a program that copies a source file to a destination file (use binary mode for any file type). Handle exceptions.

**Solution:**

```python
src = input("Source file: ")
dst = input("Destination file: ")

try:
    with open(src, "rb") as source:
        with open(dst, "wb") as dest:
            dest.write(source.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission denied.")
```

### Activity 3: CSV Reader/Writer

Given a CSV file `students.csv` with columns: `Name,Grade`, read it, compute the average grade, and write a new file `summary.txt` with the average.

**Solution:**

```python
import csv

total = 0
count = 0

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += float(row["Grade"])
        count += 1

average = total / count if count > 0 else 0

with open("summary.txt", "w") as f:
    f.write(f"Number of students: {count}\\n")
    f.write(f"Average grade: {average:.2f}\\n")

print(f"Summary written to summary.txt")
```

### Activity 4: JSON Configuration

Create a JSON file `config.json` with settings (e.g., `{"theme": "dark", "font_size": 14}`). Write a program that reads the config, allows the user to modify a setting, and saves it back.

**Solution:**

```python
import json

filename = "config.json"

# Read existing config or create default
try:
    with open(filename, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"theme": "light", "font_size": 12}

print("Current config:", config)

key = input("Enter setting to change (theme/font_size): ")
if key in config:
    value = input(f"New value for {key}: ")
    if key == "font_size":
        value = int(value)
    config[key] = value
    with open(filename, "w") as f:
        json.dump(config, f, indent=4)
    print("Config updated.")
else:
    print("Invalid setting.")
```

### Activity 5: Directory Explorer with `pathlib`

Write a program that lists all `.txt` files in a given directory (and subdirectories recursively) and prints their sizes.

**Solution:**

```python
from pathlib import Path

directory = input("Enter directory path: ")
path = Path(directory)

if not path.exists():
    print("Directory does not exist.")
else:
    for txt_file in path.rglob("*.txt"):
        size = txt_file.stat().st_size
        print(f"{txt_file} - {size} bytes")
```

---

## 8. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| `FileNotFoundError` | File path incorrect or file missing | Verify path; use `os.path.exists()` or `Path.exists()` before opening |
| `UnicodeDecodeError` | Trying to read binary file in text mode | Use binary mode (`'rb'`) or specify encoding, e.g., `open(..., encoding='utf-8')` |
| Extra blank lines in CSV output | Using `newline=''` missing on Windows | Always open CSV files with `newline=''` |
| `PermissionError` | File is open in another program, or no write permission | Close other program; check file permissions |
| File not closed properly | Forgetting `close()` or not using `with` | Use `with` statement |
| `JSONDecodeError` | Invalid JSON format | Validate JSON using a linter; ensure proper quotes and syntax |

---

## 9. Summary

- **File handling** enables persistent storage and data exchange.
- Use `open()` with modes (`r`, `w`, `a`, `b`, etc.) and always prefer the `with` context manager.
- **Paths** can be managed with `os.path` or the more modern `pathlib`.
- **CSV files** are handled by the `csv` module; use `DictReader`/`DictWriter` for dictionary access.
- **JSON files** are handled by the `json` module; use `load()`/`dump()` for files, `loads()`/`dumps()` for strings.
- Always handle file‑related exceptions to make programs robust.

---

## 10. Additional Resources

- [Python Official: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python `pathlib` Documentation](https://docs.python.org/3/library/pathlib.html)
- [Python `csv` Documentation](https://docs.python.org/3/library/csv.html)
- [Python `json` Documentation](https://docs.python.org/3/library/json.html)
- [Real Python: Reading and Writing Files](https://realpython.com/read-write-files-python/)

---