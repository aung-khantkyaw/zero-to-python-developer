# class Country :
#   def __init__(self, name, population):
#     self.name = name
#     self.population = population

# mm = Country("Myanmar", "55M")

# print(mm.name)
# print(mm.population)

# class Animals :
#   no_legs = 0

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   @classmethod
#   def set_legs(cls, new_no_lags):
#     cls.no_legs = new_no_lags

#   @staticmethod
#   def is_valid_age(self):
#     return 0 < self.age < 100

#   def walk(self):
#     print("Walking...")

# cat = Animals("Cat", 5)
# # cat.no_legs=4

# cat.set_legs(4)

# human = Animals("Human", 18)
# # human.no_legs = 2
# # print(f"Cat's Lags : {cat.no_legs}")
# # print(f"Human's Lags : {human.no_legs}")
# print(Animals.is_valid_age(cat))


# class Date:
#   def __init__(self, year, month, day):
#     self.year = year
#     self.month = month
#     self.day = day

#   @classmethod
#   def date_from_str(cls, date_str):
#     year, month, day = map(int, date_str.split('-'))
#     return cls(year, month, day) # new_date = Date(2003, 02, 18)

# new_date = Date.date_from_str('2003-02-18')

# print(new_date.year)

# class GrandFather:
#   gfMoney = 20000

# class Father(GrandFather):
#   fMoney = 30000

# class Mother:
#   mMoney = 50000

# class Son(Father, Mother):
#   Money = 500

# print(f"Son's Money : {Son.Money}")
# print(f"Father's Money : {Son.fMoney}")
# print(f"Mother's Money : {Son.mMoney}")
# print(f"GrandFather's Money : {Son.gfMoney}")

# class Animals:
#   def __init__(self, name, age, legs):
#     self.name = name
#     self.age = age
#     self.legs = legs

#   def speak(self):
#     # return "Sound"
#     raise NotImplementedError("Subclass must implement")

# class Dog(Animals):
#   def __init__(self, name, age, legs, color):
#      super().__init__(name, age, legs)
#      self.color = color

#   def speak(self):
#     return f"{self.name} says Woof!"
  
# class Cat(Animals):
#     def speak(self):
#         return f"{self.name} says Meow!"
    
# dog = Dog("Papy", 4, 4, "White")
# cat = Cat("Shwe War", 5, 4)

# # print(f"{dog.name} - {dog.age} - {dog.legs} - {dog.color}")
# print(dog.speak())

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private attribute

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

# acc = BankAccount(1000)
# acc.deposit(200)
# print(acc.get_balance())   # 1000
# # print(acc.__balance)     # AttributeError


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