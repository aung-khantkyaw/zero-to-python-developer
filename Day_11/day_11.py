# Comprehensions = for + if

# List -> [expression / for item in iterable / if ]

# for x in range(10): # 0 - 9
  # print(x**2)
  # if x % 2 != 0:
  #   print(x)

# squares = [ x**2 for x in range(10) ]
# print(squares)
# odds = [ x for x in range(10) if x % 2 != 0 ]
# print(odds)

# Dictionary -> {key_expression : value_expression / for item in iterable}

# ndarray (n - di array)

# map - map( func , iterable )
# filter - filter ( func (bool) , iterable )
# reduce - reduce( func (acumulator, current value) , iteable, init)
 
# squared = map( lambda x : x**2 , range(10)) # func_name(x) return x**2
# print(list(squared))

# 0 - 9
# step 1 : 0, x = 0, x**2 = 0
# spep 2 : 1, x = 1, x**2 = 1
# step 10 : 9, x = 9, x**2 = 81

# evens = filter( lambda x : x % 2 == 0 , range(10))
# print(list(evens))

#  0 - 9
# step 1 : 0, x = 0, 0 % 2 == 0, 0 
# step 2 : 1, x = 1, 1 % 2 != 0 

# from functools import reduce

# sum = reduce( lambda x , y : x + y  , range(4), 2 ) # func (x,y) z = x  + y , x = y , y = z
# print(sum)
# 2 , 0 - 3
# step 0 : x = 2 , y = 0 , x + y = 2
# step 1 : x = 2 , y = 1 , x + y = 3
# step 2 : x = 3 , y = 2 , x + y = 5
# step 3 : x = 5 , y = 3 , x + y = 8

# range(10) -> even -> square -> product
# 0 - 9 -> filter (0 , 2 , 4, 6, 8) -> map ( 0, 4, 16, 36, 64) -> reduce 

# from functools import reduce

# ans = reduce(
#   lambda x, y : x * y ,
#   map(
#     lambda x : x**2 ,
#     filter(
#       lambda x : x % 2 == 0,
#       range(10)
#     )
#   )
# )

# print(ans)

# func -> wrap -> func

# import time

# def timer(func):                          # decorating func
#     def wrapper(*args, **kwargs):         # func
#         start = time.time()               # before
#         result = func(*args, **kwargs)    # origin func
#         end = time.time()                 # end
#         print(f"{func.__name__} took {end - start:.4f} seconds")
#         return result 
#     return wrapper

# @timer                        # slow_function = timer(slow_function)
# def slow_function(delay):     # slow_function
#     time.sleep(delay)
#     return "Done"

# print(slow_function(2))

# from functools import wraps

# def repeat(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             '''Wrapper docstring'''
#             results = []
#             for _ in range(n):
#                 results.append(func(*args, **kwargs))
#             return results
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     '''Function docstring'''
#     return f"Hello, {name}"

# print(greet("Alice")) 

# print(greet.__name__)
# print(greet.__doc__)