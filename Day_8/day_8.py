# print("Hello")

# # print("Hello"

# try:
#   print(10/0)
# except ZeroDivisionError as e: 
#   print("Cannot divie by Zero", e)

# print("Ans")

# try:
#   10/0                              # open / input
# except ZeroDivisionError as e:
#   print(e)
# else:
#   print("ONlY TRY WORK")            # manage / operate
# finally:
#   print("ALWAYS")

# def divide(a, b):
#   if b == 0:
#     raise ZeroDivisionError("Cannot divide by zero")
#   return a / b

# try:
#   result = divide(10,0)
# except ZeroDivisionError as e:
#   raise

# import logging

# logging.basicConfig(level=logging.ERROR, filename='app.log')

# class NegativeNumberError(Exception):
#     """Raised when a negative number is encountered."""
#     pass

# def square_root(x):
#     if x < 0:
#         raise NegativeNumberError("Cannot take square root of negative number")
#     return x ** 0.5

# try:
#    print(square_root(-4))
# except NegativeNumberError as e:
#    logging.exception("A Value is Negative")
#    print(e)


file = None

try:
  file = open('app.log', 'r')
except FileNotFoundError:
  print("File Not Found")
else:
  content = file.read()
  print(content)
finally:
   file.close()