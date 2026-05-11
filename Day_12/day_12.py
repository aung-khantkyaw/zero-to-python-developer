# pip 

# numpy , pandas , mathplot

# Jupitar, Colab

# Python - list ([1, "string", bool])
# numpy - array ([ ])

import numpy as np 

# # print(np.__version__)

# # dim - 0 - n (ndarray)

# # zero = np.array(412) # 0

# # one = np.array([1, 2, 3]) # 1

# # print(zero, type(zero))
# # print(one, type(one))


# # list = [ 1, 2, 3]

# # array = np.array([1, 2, 3])

# # # print(list * 2, type(list))

# # print(array * 2, type(array))

# # print(arr * 2, type(arr))

# # one_arr = np.array((1 , 2 , 3, 5, 6, 7))
# # # two_arr = np.array( [ [1 , 2 , 3] , [ 4 , 5 , 6] ])
# # # three_arr = np.array( [ [ [1,2,3] , [4,5,6] ] , [ [7,8,9] ,  [10,11,12] ] ] )

# # # print(one_arr[2])
# # # print(two_arr[1][1])
# # # print(three_arr[1][1][1])

# # print(one_arr[1:6:2])

# # print(np.zeros((5,2)))
# # print(np.ones((5,2)))
# # print(np.full((2,2) , 'a' ))
# # print(np.eye(5))

# # np.random.seed(0)
# # print(np.random.rand(1,1))
# # print(np.random.rand(2,3))

# a = np.array([ 1, 2, 3 , 4])
# b = np.array([ 10, 12, 45, 26])

# # result = []
# # for i in range(len(a)):
# #   result.append(a[i] + b[i])

# result = a +b
# print(a < b)

# # ufuncs - universal functions - array - elements , 

# # np.sqrt(), np.exp() Unary ufuncs
# # np.add(), np.maximum() Binary ufuncs

arr = np.array([1 , 5, 6])
# print(np.sqrt(arr))

# arr = np.array([ 0, np.pi , np.pi/2])
# print(np.sin(arr))

print(np.average(arr))