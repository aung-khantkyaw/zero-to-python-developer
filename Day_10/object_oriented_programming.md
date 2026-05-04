# Module 9: Object-Oriented Programming (OOP)

**Goal:** Understand the principles of object-oriented programming and apply them to create reusable, modular code.

## 1. Introduction to OOP

Object-Oriented Programming (OOP) is a paradigm that organizes code into **objects** that contain **data** (attributes) and **behavior** (methods). It helps:

- **Model real-world entities** (e.g., a `Car` has `color` and `speed`, can `drive()`).
- **Reuse code** through inheritance.
- **Encapsulate** complexity and hide implementation details.

**Key concepts:**

- **Class** – blueprint for creating objects.
- **Object** – instance of a class.
- **Attribute** – variable that belongs to an object/class.
- **Method** – function defined inside a class.

---

## 2. Defining a Class and Creating Objects

### 2.1. Basic Class Definition

```python
class Dog:
    """A simple Dog class."""
    pass

my_dog = Dog()          # create an instance
print(type(my_dog))     # <class '__main__.Dog'>
```

### 2.2. Adding Attributes

Attributes can be set directly on an object:

```python
my_dog.name = "Buddy"
my_dog.age = 3
print(my_dog.name)   # Buddy
```

But this is not structured. Better to use `__init__`.

---

## 3. The `__init__` Method (Constructor)

`__init__` initializes an object’s state when it is created.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)   # Buddy
print(dog2.age)    # 5
```

- `self` refers to the instance being created.
- Attributes set with `self` are **instance attributes** (each object has its own copy).

---

## 4. Instance Methods

Methods are functions defined inside a class that operate on the instance.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_human_years(self):
        return self.age * 7

dog = Dog("Buddy", 3)
dog.bark()                     # Buddy says Woof!
print(dog.get_human_years())   # 21
```

---

## 5. Class Attributes and Class Methods

### 5.1. Class Attributes

Attributes shared by all instances of a class.

```python
class Dog:
    species = "Canis familiaris"   # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Dog.species)   # Canis familiaris (accessible via class)
dog = Dog("Buddy", 3)
print(dog.species)   # Also accessible via instance
```

### 5.2. Class Methods

Use `@classmethod` decorator. The first parameter is `cls` (the class itself).

```python
class Dog:
    species = "Canis familiaris"

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species())   # Canis familiaris
```

### 5.3. Static Methods

Use `@staticmethod` – no `self` or `cls`. Used for utility functions related to the class.

```python
class Dog:
    @staticmethod
    def is_valid_age(age):
        return 0 < age < 30

print(Dog.is_valid_age(5))   # True
```

---

## 6. Inheritance

Inheritance allows a class (child) to reuse attributes and methods from another class (parent).

### 6.1. Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())   # Buddy says Woof!
print(cat.speak())   # Whiskers says Meow!
```

### 6.2. Using `super()`

`super()` calls a method from the parent class, useful to extend parent behavior.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {name} created.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent __init__
        self.breed = breed
        print(f"Dog of breed {breed} created.")

dog = Dog("Buddy", "Golden Retriever")
# Output:
# Animal Buddy created.
# Dog of breed Golden Retriever created.
```

### 6.3. Method Overriding

Child classes can override parent methods.

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Dog.speak overrides Animal.speak
```

---

## 7. Encapsulation and Properties

Encapsulation hides internal data and provides controlled access through methods.

### 7.1. Name Mangling (Private Attributes)

Use `__` prefix to make an attribute “private” (name mangling).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount(1000)
print(acc.get_balance())   # 1000
# print(acc.__balance)     # AttributeError
```

**Note:** Name mangling doesn’t enforce privacy, but it discourages direct access.

### 7.2. Properties (`@property`)

Use `@property` to define getters and setters for a more Pythonic approach.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # protected attribute (convention)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)        # 25
temp.celsius = 30          # setter called
print(temp.fahrenheit)     # 86.0
```

---

## 8. Magic (Dunder) Methods

Magic methods have double underscores (`__method__`). They define how objects behave with built-in operations.

| Method                 | Description                                     |
| ---------------------- | ----------------------------------------------- |
| `__init__(self, ...)`  | Constructor                                     |
| `__str__(self)`        | String representation for end‑users (`print()`) |
| `__repr__(self)`       | Unambiguous representation for developers       |
| `__len__(self)`        | Returns length (used by `len()`)                |
| `__add__(self, other)` | Defines behavior for `+`                        |
| `__eq__(self, other)`  | Defines behavior for `==`                       |

**Example:**

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

book = Book("1984", "George Orwell", 328)
print(book)                # 1984 by George Orwell (__str__)
print(repr(book))          # Book('1984', 'George Orwell', 328)
print(len(book))           # 328
```

---

## 9. Polymorphism and Duck Typing

**Polymorphism** allows objects of different classes to be treated uniformly if they implement the same method interface. Python uses **duck typing** – “if it walks like a duck and quacks like a duck, it’s a duck”.

```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Car:
    def horn(self):
        return "Beep!"

def make_sound(animal):
    print(animal.sound())   # only cares that .sound() exists

make_sound(Dog())   # Woof!
make_sound(Cat())   # Meow!
# make_sound(Car())   # AttributeError (Car has no sound())
```

With inheritance:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())   # Woof, Meow (same method name, different behaviors)
```

---

## 10. Abstract Base Classes (ABC)

An **abstract class** cannot be instantiated. It defines methods that subclasses **must** implement. Use the `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()   # TypeError: Can't instantiate abstract class
rect = Rectangle(4, 5)
print(rect.area())      # 20
```

If a subclass does not implement all abstract methods, it also becomes abstract and cannot be instantiated.

---

## 11. Multiple Inheritance and MRO

Python supports **multiple inheritance** (a class inherits from more than one parent). The **Method Resolution Order (MRO)** defines the order in which parent classes are searched for methods. Use `ClassName.__mro__` to inspect.

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):   # A comes before B
    pass

c = C()
c.show()   # A (because A is first in MRO)
print(C.__mro__)   # (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
```

### Mixin Classes

A mixin provides small, reusable functionality and is not meant to stand alone.

```python
class LoggerMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")

class User(LoggerMixin):
    def __init__(self, name):
        self.name = name
        self.log(f"User {name} created")

u = User("Mg Mg")   # [LOG] User Mg Mg created
```

---

## 12. Composition (Has‑a Relationship)

Instead of inheriting from a class (**is‑a**), a class can contain instances of other classes (**has‑a**). Composition often leads to more flexible designs than deep inheritance.

```python
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Car:
    def __init__(self):
        self.engine = Engine()   # composition
        self.wheels = Wheels()

    def drive(self):
        return f"{self.engine.start()} and {self.wheels.rotate()}"

car = Car()
print(car.drive())   # Engine started and Wheels rotating
```

**When to prefer composition over inheritance:**
- The relationship is “has‑a” rather than “is‑a”.
- You need to change behavior at runtime.
- Inheritance hierarchy would become deep and fragile.

---

## 13. Dataclasses (Python 3.7+)

Writing classes that primarily store data requires a lot of boilerplate (`__init__`, `__repr__`, `__eq__`). The `@dataclass` decorator generates these automatically.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = "default@example.com"   # default value

p1 = Person("Aung", 25)
p2 = Person("Aung", 25)
print(p1)               # Person(name='Aung', age=25, email='default@example.com')
print(p1 == p2)         # True (auto-generated __eq__)
```

It also supports `__hash__`, `__repr__`, `__init__`, and optional ordering. Great for data containers (DTOs, value objects).

---

## 14. Hands‑On Activities

### Activity 1: Simple Class – Rectangle

Create a class `Rectangle` with attributes `width` and `height`. Include methods:

- `area()` returns area.
- `perimeter()` returns perimeter.
- `__str__` returns a readable description.

**Solution:**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

rect = Rectangle(5, 3)
print(rect)                # Rectangle(width=5, height=3)
print(rect.area())         # 15
print(rect.perimeter())    # 16
```

### Activity 2: Inheritance – Vehicle Hierarchy

Create a base class `Vehicle` with `make`, `model`, and a method `info()`. Create subclasses `Car` and `Motorcycle`. Car has `num_doors`, Motorcycle has `has_sidecar`. Override `info()` to include specific details.

**Solution:**

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def info(self):
        return f"{super().info()}, {self.num_doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def info(self):
        sidecar = "with sidecar" if self.has_sidecar else "no sidecar"
        return f"{super().info()}, {sidecar}"

car = Car("Toyota", "Camry", 4)
bike = Motorcycle("Harley", "Sportster", False)
print(car.info())     # Toyota Camry, 4 doors
print(bike.info())    # Harley Sportster, no sidecar
```

### Activity 3: Encapsulation – Bank Account

Create a class `BankAccount` with a private attribute `__balance`. Provide methods:

- `deposit(amount)` adds if positive.
- `withdraw(amount)` subtracts if sufficient funds.
- `get_balance()` returns balance.
- Use property to allow read-only access to balance.

**Solution:**

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    @property
    def balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)   # 1300
```

### Activity 4: Magic Methods – Vector Class

Create a class `Vector` that represents a 2D vector. Implement:

- `__init__(x, y)`
- `__add__(other)` returns new Vector.
- `__sub__(other)`
- `__mul__(scalar)`
- `__eq__(other)`
- `__str__` and `__repr__`

**Solution:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)               # Vector(6, 8)
print(v1 * 3)           # Vector(6, 9)
print(v1 == Vector(2, 3))   # True
```

### Activity 5: Class Method and Static Method

Create a class `Person` with:

- Instance attributes: `name`, `age`.
- Class attribute: `population` (count of instances).
- `__init__` increments population.
- Class method `get_population()`.
- Static method `is_adult(age)` returns True if age >= 18.

**Solution:**

```python
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

p1 = Person("Alice", 25)
p2 = Person("Bob", 17)
print(Person.get_population())   # 2
print(Person.is_adult(20))       # True
print(Person.is_adult(16))       # False
```

---

## 15. Common Pitfalls & Troubleshooting

| Problem                                                        | Likely Cause                                                     | Solution                                                     |
| -------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| `TypeError: __init__() missing 1 required positional argument` | Forgetting to pass required arguments when creating object       | Check class `__init__` parameters; provide all required args |
| AttributeError: object has no attribute `__balance`            | Trying to access private attribute directly                      | Use getter/setter or property, not direct name               |
| Infinite recursion in property setter                          | Setter calls itself (e.g., `self.balance = value` inside setter) | Use a different internal name (e.g., `_balance`)             |
| Method overriding but forgetting to call `super()`             | Losing parent initialization                                     | Call `super().__init__()` if parent needs setup              |
| `self` missing in method definition                            | Forgetting `self` as first parameter                             | Always include `self` for instance methods                   |

---

## 16. Summary

- **Classes** are blueprints; **objects** are instances.
- `__init__` initializes instance attributes.
- **Instance methods** operate on an object; **class methods** operate on the class.
- **Inheritance** allows reuse and extension.
- **Encapsulation** hides internal data; use properties (`@property`) for controlled access.
- **Magic methods** enable custom behavior for built-in operations.
- **Polymorphism** allows different classes to be used through a common interface.
- **Abstract base classes** enforce method implementation in subclasses.
- **Multiple inheritance** requires understanding MRO; mixins are a practical use.
- **Composition** (has‑a) is often more flexible than deep inheritance.
- `__slots__` reduces memory for many instances.
- **Dataclasses** reduce boilerplate for data containers.
- OOP helps structure code, reduce duplication, and model real-world concepts.

---

## 17. Additional Resources

- [Python Official: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python `property` Documentation](https://docs.python.org/3/library/functions.html#property)
- [Magic Methods Guide](https://rszalski.github.io/magicmethods/)
- [ABC Module Documentation](https://docs.python.org/3/library/abc.html)
- [Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
```