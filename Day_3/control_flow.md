# Module 3: Control Flow

**Goal:** Enable students to control the execution flow of their programs using conditional statements and loops.

## 1. Conditional Statements: `if`, `elif`, `else`

Conditionals allow the program to execute different blocks of code based on certain conditions.

### 1.1. The `if` Statement

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

- The condition must evaluate to a boolean (`True` or `False`).
- The code block is indented (usually 4 spaces).

### 1.2. `ifelse`

```python
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### 1.3. `ifelifelse`

Use `elif` (short for “else if”) to check multiple conditions.

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")
```

### 1.4. Nested Conditionals

You can place conditionals inside other conditionals.

```python
if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Too young to vote")
```

**Best Practice:** Avoid deep nesting by using logical operators or restructuring code.

### 1.5. Conditional Expressions (Ternary Operator)

A compact way to write simple if‑else.

```python
status = "Adult" if age >= 18 else "Minor"
```

---

## 2. Loops

Loops repeat a block of code multiple times.

### 2.1. `for` Loop – Iterating Over Sequences

The `for` loop is used to iterate over any iterable (list, string, range, etc.).

```python
# Over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Over a string
for char in "Python":
    print(char)

# Using range()
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2): # start, stop, step → 2,4,6,8
    print(i)
```

### 2.2. `while` Loop – Condition‑Based Repetition

The `while` loop continues as long as a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1   # Important: update the condition to avoid infinite loop
```

### 2.3. Infinite Loops and How to Avoid Them

An infinite loop runs forever if the condition never becomes `False`.

```python
# This will run forever
count = 0
while count < 5:
    print(count)   # forgot to increment count
```

- Always ensure the loop variable is updated.
- Use `Ctrl+C` to break out of an infinite loop in the terminal.

---

## 3. Loop Control Statements

### 3.1. `break` – Exit the Loop Entirely

```python
for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0,1,2,3,4
```

### 3.2. `continue` – Skip the Current Iteration

```python
for i in range(5):
    if i == 2:
        continue
    print(i)   # prints 0,1,3,4
```

### 3.3. `else` Clause with Loops

The `else` block executes **only if** the loop completes normally (i.e., not terminated by `break`).

```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break")   # Executes

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't run because break occurred")
```

**Use case:** Useful for searching – if you find an item, `break`; otherwise, run `else`.

---

## 4. Nested Loops

A loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

```python
for i in range(3):      # outer loop
    for j in range(2):  # inner loop
        print(f"i={i}, j={j}")
```

**Output:**

```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

---

## 5. Simple Pattern Printing

Nested loops are commonly used to print patterns.

### 5.1. Right‑angled Triangle

```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```

Output:

```
*
**
***
****
*****
```

### 5.2. Square

```python
size = 5
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()
```

Output:

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### 5.3. Pyramid

```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```

Output:

```
    *
   ***
  *****
 *******
*********
```

---

## 6. Hands‑On Activities

### Activity 1: Grading System

Write a program that:

- Asks the user for a score (0–100).
- Prints the letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60).
- If the score is out of range, print an error message.

**Solution:**

```python
score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

### Activity 2: Sum of Numbers

Ask the user for a positive integer `n` and calculate the sum of all numbers from 1 to `n` using both a `for` loop and a `while` loop.

**Solution (for loop):**

```python
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum: {total}")
```

**Solution (while loop):**

```python
n = int(input("Enter a positive integer: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum: {total}")
```

### Activity 3: Guess the Number Game

- Generate a random number between 1 and 10 (use `random.randint`).
- Let the user guess until they get it right.
- After each guess, tell them if it's too high or too low.
- Count the number of attempts and display it when they guess correctly.
- Use `break` to exit the loop when correct.

**Solution:**

```python
import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10): "))
    attempts += 1
    if guess == secret:
        print(f"Correct! It took you {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

### Activity 4: Multiplication Table

Ask the user for a number and print its multiplication table from 1 to 10.

**Solution:**

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Activity 5: Pattern Printing

Print the following pattern using nested loops:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Solution:**

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

## 7. Common Pitfalls & Troubleshooting

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| Infinite loop | Condition never becomes `False` or loop variable not updated | Ensure the variable changes inside the loop; add a `break` condition if needed |
| `IndentationError` | Mixed tabs/spaces or incorrect indentation | Use consistent spaces (4 per level) |
| Off‑by‑one errors | Wrong range endpoints or loop condition | Check start/stop values carefully; test with small numbers |
| `break` not working as expected | `break` placed outside loop or inside nested loop incorrectly | `break` only exits the innermost loop; use flags if needed |
| Forgetting to convert input | Using `input()` directly in numeric comparison | Use `int(input())` or `float(input())` |
| `else` with loops confusion | Thinking `else` runs when condition is `False` (it runs when no `break`) | Clarify that `else` is executed if loop ends normally |

---

## 8. Summary

- **Conditionals:** `if`, `elif`, `else` allow branching based on boolean expressions.
- **Loops:**
    - `for` iterates over sequences or ranges.
    - `while` repeats while a condition is true.
- **Control statements:**
    - `break` exits the loop.
    - `continue` skips the rest of the current iteration.
    - `else` executes only if the loop wasn’t terminated by `break`.
- **Nested loops** enable complex iterations and pattern generation.

---

## 9. Additional Resources

- [Python Official: `if` Statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Official: `for` Statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Official: `while` Statement](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Real Python: Python Loops](https://realpython.com/python-for-loop/)

---