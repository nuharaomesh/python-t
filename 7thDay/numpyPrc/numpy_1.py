import numpy as np

# Creating a array actually a list but technically its a numpy array
numpy_arr_1 = np.array([1, 2, 3, 4, 5])
# Same as list we can access element by there index number
print(numpy_arr_1[0])
numpy_arr_2 = np.array([1, 2, 3, 4, 5])

# print(numpy_arr)
# # The type is numpy ndarray
print(type(numpy_arr))

# We can do some arithmetic ops with numpy arrays
addition_of_arr = numpy_arr_1 + numpy_arr_2
subtract_of_arr = numpy_arr_1 - numpy_arr_2
multiply_of_arr = numpy_arr_1 * numpy_arr_2
divide_of_arr = numpy_arr_1 / numpy_arr_2

print(addition_of_arr)
print(subtract_of_arr)
print(multiply_of_arr)
print(divide_of_arr)

# numpy library other functions
# Square root 
result_sqrt = np.sqrt(numpy_arr_1)
print(result_sqrt)

# Summation 
result_sum = np.sum(numpy_arr_1)
print(result_sum)

# Mean (Average)
result_mean = np.mean(numpy_arr_1)
print(result_mean)

# Maximum and Minimum

result_max = np.max(numpy_arr_1)
print(result_max)

result_min = np.min(numpy_arr_1)
print(result_min)