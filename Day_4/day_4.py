# # empty_list = []

# # nested = [
# #   [1 , 2 , 3],
# #   [4 , 5 , 6],
# # ]
# # # numpy.array (type - ndarray)

# # Searching, Sorting, CRUD

# fruits = ["apple", "egg" , "cherry", "date" , "banana", "banana" ]
# # fruits = ['apple', 'egg' , 'cherry' ]
# # raw = fruits.copy()  # ['apple', 'egg' , 'cherry' ]

# # raw.append('date')

# # print(fruits)
# # print(raw)

# # print(fruits[0]) # apple
# # print(fruits[-1]) # date
# # print(fruits[1:3]) # banana , cherry    # stop - 1
# # print(fruits[::3])

# # print(fruits.count("apple"))


# # number = [285 , 458, 28]
# # fruits.sort() # ['apple', 'cherry', 'egg']
# # print(fruits)

# # fruits.reverse() # ['egg', 'cherry', 'apple']
# # print(fruits)

# # fruits.clear()
# # print(fruits)

# # list

# # a = list.sort() - x
# # print(list.sort()) - x

# # list.sort()
# # print(list)

# # x-expression for x in range(1, 6)

# print(fruits)
# for i, fruit in fruits:
#   print(fruit)

# empty_tuple = ()
# # point = (x, y)
# point = (95 , 16, 95)
# single = (5,)
# print(type(single))

# print(point.index(95))

# empty_dict = {}

# # person = {"name": "Alice", "age": 25, "city": "New York"}

# # Using dict() constructor
# # person = dict(name="Alice", age=25)

# person = {
#   "name": "Alice", 
#   "age": 25, 
#   "roll-no": 25,
#   "city": "New York",
# }
# person2 = person.copy()

# print(person)
# print(person2)
# # print(person)

# # person["age"] = 30
# # person["job"] = "Student"
# # del person["isSingle"]

# # print(person)

# # print(person.keys()) # keys
# # print(person.values()) # values
# # print(person.items()) # keys , values

# alice = {
#   "isSingle": True
# }

# person2.update(alice)
# # person.clear()

# print(person)
# print(person2)

# empty = set()
# number = { 1 , 2 , 4 , 4 }

# number.add(3)
# number.remove(4)
# print(number)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(B - A) # join - left right
print(A ^ B)

print(A >= B)