# age = 20
# citizen = False

# if age >= 18:
#     if citizen:
#         print("Eligible to vote")
#     else:
#         print("Not eligible to vote")
# else:
#     print("Too young to vote")

# and or not

# if not(citizen):
#   print("Eligible to vote")
# else:
#   print("Not eligible to vote")

# conditional ? "true" : "false"

# "true" conditional "false"

# status = "Adult" if age >= 18 else "Minor"

# print(status)

# it_accessories = ['laptop' , 'phone', 'powerbank', 'cable', 'tablet']

# for ( pronoun ) in (data resources)
# for it_accessory in it_accessories:
#   print(it_accessory, end=" ")

# for i in range(2, 10, 2): # 2 5 8 
#   print(i, end=" ")

# while => work true

# start
# while(end)
#   step

# count = 0

# # until count under 5

# while count < 5:
#   print(count)
#   count += 1

# for i in range(10): # 0 1 2 3 4 (5) 6 7 8 9
#   if i == 5:
#     continue
#   print(i)
#  --------------------------
# print("End loop ...")

# num_list = [1, 5, 8, 6, 7]
# search = 7

# for i in num_list:
#   print(i)
#   if i == search:
#     print("Found!")
#     break
# else:
#   print("Not Found")

# print('End loop')

# for i in range(3):      # outer loop
#     print(f"i : {i}")
#     for j in range(2):  # inner loop
#         print(f"j : {j}")
#     print('-------------------------------')

rows = 5
for i in range(1, rows + 1):
  print("*" * i)
