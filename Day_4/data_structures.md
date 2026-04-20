# Module 4: Data Structures

**Goal:** Understand Python’s built‑in data structures and choose the right one for different tasks.

## 1. Introduction to Data Structures

Data structures are containers that organize and store data efficiently. Python provides four built‑in data structures:

| Structure      | Ordered    | Mutable | Allows Duplicates     | Use Case                                       |
| -------------- | ---------- | ------- | --------------------- | ---------------------------------------------- |
| **List**       | Yes        | Yes     | Yes                   | Ordered collection, frequent modifications     |
| **Tuple**      | Yes        | No      | Yes                   | Fixed data, lightweight, keys for dictionaries |
| **Dictionary** | Yes (3.7+) | Yes     | Keys: no; Values: yes | Fast lookups by key                            |
| **Set**        | No         | Yes     | No                    | Unique items, membership tests                 |

---

## 2. Lists

Lists are ordered, mutable sequences. They can hold items of different types.

### 2.1. Creating Lists

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]
```

### 2.2. Accessing Elements (Indexing & Slicing)

Same as string indexing.

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])      # "apple"
print(fruits[-1])     # "date"
print(fruits[1:3])    # ["banana", "cherry"]
print(fruits[::2])    # ["apple", "cherry"]
```

### 2.3. Common List Methods

| Method                | Description                                      | Example                           |
| --------------------- | ------------------------------------------------ | --------------------------------- |
| `append(item)`        | Adds item to the end                             | `fruits.append("elderberry")`     |
| `insert(index, item)` | Inserts at position                              | `fruits.insert(1, "blueberry")`   |
| `extend(iterable)`    | Adds all items from iterable                     | `fruits.extend(["fig", "grape"])` |
| `remove(item)`        | Removes first occurrence                         | `fruits.remove("banana")`         |
| `pop(index)`          | Removes and returns item at index (default last) | `last = fruits.pop()`             |
| `index(item)`         | Returns index of first occurrence                | `pos = fruits.index("cherry")`    |
| `count(item)`         | Counts occurrences                               | `cnt = fruits.count("apple")`     |
| `sort()`              | Sorts in place                                   | `numbers.sort()`                  |
| `reverse()`           | Reverses in place                                | `numbers.reverse()`               |
| `clear()`             | Removes all items                                | `fruits.clear()`                  |
| `copy()`              | Returns shallow copy                             | `fruits2 = fruits.copy()`         |

**Examples:**

```python
colors = ["red", "blue", "green"]
colors.append("yellow")
colors.insert(1, "orange")
print(colors)  # ["red", "orange", "blue", "green", "yellow"]

colors.sort()
print(colors)  # ["blue", "green", "orange", "red", "yellow"]
```

### 2.4. List Comprehensions

A concise way to create lists.

```python
# Create list of squares
squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]   # [2, 4, 6, 8, 10]
```

### 2.5. Iterating Over Lists

```python
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

---

## 3. Tuples

Tuples are **immutable** sequences. Once created, they cannot be changed.

### 3.1. Creating Tuples

```python
empty = ()
point = (10, 20)
single = (5,)   # Note the comma; otherwise it's just int
```

### 3.2. Accessing Elements (Indexing & Slicing)

Same as lists, but no modification.

```python
point = (10, 20)
print(point[0])   # 10
```

### 3.3. Why Use Tuples?

- **Immutability** ensures data cannot be accidentally changed.
- **Performance** – slightly faster than lists.
- **Dictionary keys** – only immutable types can be keys (tuples can, lists cannot).
- **Return multiple values** from functions.

### 3.4. Tuple Packing and Unpacking

```python
# Packing
coordinates = 10, 20, 30   # parentheses optional

# Unpacking
x, y, z = coordinates      # x=10, y=20, z=30

# Swapping variables
a, b = b, a
```

### 3.5. Methods

Tuples have only two methods: `count()` and `index()`.

---

## 4. Dictionaries

Dictionaries store key‑value pairs. Keys must be immutable (string, number, tuple). Values can be any type.

### 4.1. Creating Dictionaries

```python
empty = {}
person = {"name": "Alice", "age": 25, "city": "New York"}

# Using dict() constructor
person = dict(name="Alice", age=25)
```

### 4.2. Accessing Values

```python
print(person["name"])      # "Alice"
print(person.get("age"))   # 25
print(person.get("country", "Unknown"))  # "Unknown" (default)
```

### 4.3. Modifying Dictionaries

```python
person["age"] = 26          # update
person["job"] = "Engineer"  # add
del person["city"]          # delete

# Remove and return value
age = person.pop("age")

# Get and remove last inserted item (Python 3.7+)
item = person.popitem()
```

### 4.4. Dictionary Methods

| Method               | Description                        |
| -------------------- | ---------------------------------- |
| `keys()`             | Returns view of keys               |
| `values()`           | Returns view of values             |
| `items()`            | Returns view of (key, value) pairs |
| `update(other_dict)` | Merges another dictionary          |
| `clear()`            | Removes all items                  |
| `copy()`             | Shallow copy                       |

**Examples:**

```python
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

### 4.5. Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(1, 6)}   # {1:1, 2:4, 3:9, 4:16, 5:25}
```

---

## 5. Sets

Sets are unordered collections of **unique** elements. They support mathematical set operations.

### 5.1. Creating Sets

```python
empty = set()          # Note: {} creates empty dict
numbers = {1, 2, 3, 3}   # {1, 2, 3} (duplicates removed)
from_list = set([1, 2, 2, 3])   # {1, 2, 3}
```

### 5.2. Adding and Removing Elements

```python
numbers.add(4)
numbers.remove(2)     # raises KeyError if not present
numbers.discard(5)    # no error if not present
numbers.pop()         # removes and returns an arbitrary element
numbers.clear()
```

### 5.3. Set Operations

| Operation            | Method                   | Operator |
| -------------------- | ------------------------ | -------- |
| Union                | `union()`                | `\|`     |
| Intersection         | `intersection()`         | `&`      |
| Difference           | `difference()`           | `-`      |
| Symmetric Difference | `symmetric_difference()` | `^`      |
| Subset               | `issubset()`             | `<=`     |
| Superset             | `issuperset()`           | `>=`     |

**Examples:**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # {1,2,3,4,5,6}
print(A & B)   # {3,4}
print(A - B)   # {1,2}
print(A ^ B)   # {1,2,5,6}
```

### 5.4. Set Comprehensions

```python
squares = {x**2 for x in range(1, 6)}   # {1,4,9,16,25}
```

---

## 6. Choosing the Right Data Structure

| Task                                                           | Recommended Structure |
| -------------------------------------------------------------- | --------------------- |
| Store ordered collection, allow duplicates, need modifications | List                  |
| Store fixed data, need immutability (e.g., dictionary keys)    | Tuple                 |
| Look up values by unique key                                   | Dictionary            |
| Ensure uniqueness, test membership efficiently                 | Set                   |

---

## 7. Hands‑On Activities

### Activity 1: List Manipulation

Create a list of 5 numbers. Perform the following:

1. Append a new number at the end.
2. Insert a number at index 2.
3. Remove the third element.
4. Sort the list in descending order.
5. Create a new list with squares of all numbers using list comprehension.

**Solution:**

```python
nums = [5, 2, 8, 1, 9]
nums.append(3)
nums.insert(2, 7)
nums.pop(2)   # or del nums[2]
nums.sort(reverse=True)
squares = [x**2 for x in nums]
print(squares)
```

### Activity 2: Tuple Unpacking

Write a function that returns both the minimum and maximum of a list. Use tuple unpacking to assign the results.

**Solution:**

```python
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [4, 7, 2, 9, 5]
minimum, maximum = min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")
```

### Activity 3: Phonebook using Dictionary

Create a phonebook dictionary (name → phone number). Provide a menu to:

- Add contact
- Search contact
- Delete contact
- Display all contacts

**Solution:**

```python
phonebook = {}

while True:
    print("\\n1. Add contact\\n2. Search\\n3. Delete\\n4. Display\\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone: ")
        phonebook[name] = number
        print("Added.")
    elif choice == "2":
        name = input("Name: ")
        print(phonebook.get(name, "Not found"))
    elif choice == "3":
        name = input("Name: ")
        if name in phonebook:
            del phonebook[name]
            print("Deleted.")
        else:
            print("Not found.")
    elif choice == "4":
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
```

### Activity 4: Set Operations

Given two lists, find:

- Common elements (intersection)
- Elements in list1 but not in list2 (difference)
- All unique elements from both lists (union)

**Solution:**

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
diff = set1 - set2
union = set1 | set2

print("Common:", common)
print("Only in list1:", diff)
print("All unique:", union)
```

### Activity 5: Word Frequency Counter

Write a program that reads a sentence from the user and counts the frequency of each word (case‑insensitive, ignore punctuation).

**Solution:**

```python
sentence = input("Enter a sentence: ").lower()
# Remove punctuation (simple approach)
for p in ".,!?;:":
    sentence = sentence.replace(p, "")

words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word}: {count}")
```

---

## 8. Common Pitfalls & Troubleshooting

| Problem                                                               | Likely Cause                                          | Solution                                                                                             |
| --------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `TypeError: unhashable type: 'list'`                                  | Trying to use a list as dictionary key or set element | Use tuple instead if immutability is needed                                                          |
| `KeyError`                                                            | Accessing missing dictionary key with `[]`            | Use `.get()` to provide default or check with `in`                                                   |
| Modifying list while iterating                                        | Skipping elements or causing runtime error            | Iterate over a copy (`for item in list[:]:`) or use list comprehension                               |
| Confusion between `list.remove()` and `list.pop()`                    | `remove()` deletes by value, `pop()` by index         | Remember: `remove()` raises error if value missing; `pop()` returns removed item                     |
| Duplicates in set not automatically handled when converting from list | Not realizing set removes duplicates                  | Use `set(list)` to deduplicate                                                                       |
| Order of items in set or dict not guaranteed (pre‑3.7)                | Assuming order                                        | In Python 3.7+, dict maintains insertion order; sets are unordered. Use `sorted()` if order matters. |

---

## 9. Summary

- **Lists** – ordered, mutable, allow duplicates. Use for general collections.
- **Tuples** – ordered, immutable. Use for fixed data, dictionary keys, multiple returns.
- **Dictionaries** – key‑value mappings, fast lookups. Keys must be immutable.
- **Sets** – unordered, unique elements. Use for membership tests and set operations.
- Choose the right structure based on whether you need order, mutability, uniqueness, and key‑value mapping.

---

## 10. Additional Resources

- [Python Official: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python: Dictionaries](https://realpython.com/python-dicts/)
- [Real Python: Sets](https://realpython.com/python-sets/)

---
