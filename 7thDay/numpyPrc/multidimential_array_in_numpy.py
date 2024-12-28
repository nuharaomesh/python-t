import numpy as np

# Multidimensional arrays in numpy
# 2D arrays
arr = np.array([[1, 2], [2, 3], [3, 4]])
print(arr[0][1])

# 3D arrays
                                                                    # we can also define the type of elements that need to be 
arr = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=float)
print(type(arr))
print(arr[0, 1, 1])

# This shape attribute describe its dimensions
print(arr.shape)

# with dtype attribute specifies the data types of the elements that stored in the Numpy array
print(arr.dtype)

# In size attribute its describe the elements count that hold in the numpy array
print(arr.size)

# The ndim attribute indicates the number of dimensions (axes) in the array
print(arr.ndim)

# Boolean indexing
arr = np.array([23, 12, 43, 2, 24, 21])
# This is the most powerful feature in numpy for data manipulation, as it enables the selection of specific elements without the need for loops.
condition = arr > 20
# Returning the bool array 
print(condition)

# Filtering the condition bool list and filtering True elements only and return that True element as them before
# Also instead of doing this we can do this with short form like below
filtered = arr[condition]
filtered = arr[arr > 20]

# Combining multiple condition with logical operators (&, |, ~)
filtered = arr[(arr < 25) & (arr > 0)]
print(filtered)

