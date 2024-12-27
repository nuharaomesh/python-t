import numpy as np

# Multidimensional arrays in numpy
# 2D arrays
arr = np.array([[1, 2], [2, 3], [3, 4]])
print(arr[0][1])

# 3D arrays
                                                                    # we can also define the type of elements that need to be 
arr = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=float)
print(type(arr))
print(arr[0][1][1])

# This shape attribute describe its dimensions
print(arr.shape)

# with dtype attribute specifies the data types of the elements that stored in the Numpy array
print(arr.dtype)

# In size attribute its describe the elements count that hold in the numpy array
print(arr.size)

# The ndim attribute indicates the number of dimensions (axes) in the array
print(arr.ndim)