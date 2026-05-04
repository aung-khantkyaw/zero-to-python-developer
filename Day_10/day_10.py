# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):  # User
#         return f"{self.title} by {self.author}" 

#     def __repr__(self): # Developer
#         return f"Book('{self.title}', '{self.author}', {self.pages})"
    
#     def __len__(self):
#         return self.pages
    
#     def __eq__(self, other):
#         if not isinstance(other, Book):
#             return NotImplemented
#         return self.title == other.title and self.author == other.author and self.pages == other.pages
    
# book1 = Book("1984", "George Orwell", 328)
# book2 = Book("1984", "George Orwell", 328)
# # print(book)                # 1984 by George Orwell (__str__)
# # print(repr(book))          # Book('1984', 'George Orwell', 328)

# print(book1 == book2)

# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __add__(self, other):
#     return Point(self.x + other.x, self.y + other.y)
    
# p1 = Point(1, 2)
# p2 = Point(3, 4)

# p3 = p1 + p2

# print(p3.x, p3.y)

# class Animal:
#   def speak(self):
#     pass

# class Dog(Animal):
#   def speak(self):
#     return "Woof"
  
# class Cat(Animal):
#   def speak(self):
#     return "Meow"

# animals = [Dog(), Cat()]
# for a in animals:
#   print(a.speak())


# ABC - must implement
# form abc import ABC, abstractmethod


# from abc import ABC, abstractmethod

# class Shape(ABC):
#   @abstractmethod
#   def area(self):
#     pass

#   @abstractmethod
#   def perimeter(self):
#     pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#        return 2 * (self.width + self.height)

# class Circle(Shape):
#     def __init__(self,r):
#         self.r= r

#     def area(self):
#        return 3.14 * (self.r ** 2)
    
# rect = Rectangle(4, 5)
# circ = Circle(5)
# print(rect.area())

# C3 Linearization Algo (MRO)

# class Father:
#   Money = 30000

# class Mother:
#   pass

# class Son(Mother, Father):
#   pass

# print(Son.Money)

# print(Son.__mro__)

# class Engine:
#     def start(self):
#         return "Engine started"

# class Wheels:
#     def rotate(self):
#         return "Wheels rotating"

# class Car:
#     def __init__(self):
#         self.engine = Engine()   # composition
#         self.wheels = Wheels()

#     def drive(self):
#         return f"{self.engine.start()} and {self.wheels.rotate()}"

# car = Car()
# print(car.drive())   # Engine started and Wheels rotating

# class Vehicle:
#     pass

# class DiselEngine:
#     def start(self):
#         return "Diesel Engine started"
    
# class ElecEngine:
#     def start(self):
#         return "Electric Engine started"
    
# class NucEngine:
#     def start(self):
#         return "Nuc Engine started"

# class Wheels:
#     def rotate(self):
#         return "Wheels rotating"
    
# class Car(Vehicle):
#     def __init__(self, engine_type):
#         self.engine = engine_type
#         self.wheels = Wheels()

#     def drive(self):
#         return f"{self.engine.start()} and {self.wheels.rotate()}"

# car = Car(NucEngine())
# print(car.drive())   # Engine started and Wheels rotating

from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int
  email: str = "example@gmail.com"

p0 = Person("Aung", 23)
p1 = Person("Aung", 23)
p2 = Person("Khant", 17, "khant@gmail.com")

print(p0 == p1)