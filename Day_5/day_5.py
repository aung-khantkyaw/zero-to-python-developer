'''
def func_name(<parameter(s)>) : #
  """ Document Strings """
  func_body #
  return <value> ##

func_name(<argument(s)>)
'''

def greeting(name, greeting = "Hello"): # deef greeting(greeting="Hello" , name) X
  print(f"{greeting}! {name} ")

# greeting("Aung", "Hi") # Positional Argu 
# greeting(greeting="Hi", name="Aung") # Keyword

# greeting(name="Aung")

# sum( a + b )
def sum_all(*args) : # tuple ()
  """ summ all arguments input """
  print(args, type(args))
  return sum(args)

# print(f"sum all : ", sum_all(1 , 2 , 3 , 4 , 5 , 6))

person = {}

def create_person(**kwargs): # dictionary {}
  person.update(kwargs)
  return person

# print(create_person(name="Aung", age=23))

def min_max(numbers):
    return min(numbers), max(numbers)

# minimum, maximum = min_max([4, 2, 9, 1])
# print(minimum, maximum) 

# def my_func():
#    x = 10
#    print(x)

# my_func()

# print(x)

# count = 0

# def increment():
#    global count
#    count += 1

# increment()
# print(count)

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)

# outer()

# lambda arguments : expression

def square(x):
   return x ** 2

square_lambda = lambda x : x ** 2

print(square(5))
print(square_lambda(5))

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

print(squared)




print(help(sum))
print(sum.__doc__)

'''
def func_name(n):
  if end-
    return
  else
   func_name(n - 1)
   return
'''

def factorial(n):
    """Return n! (n factorial) using recursion."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))