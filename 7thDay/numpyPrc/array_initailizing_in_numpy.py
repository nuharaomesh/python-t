import numpy as np

# Creating and initializing 0 value for every element with np.zeros() function
arr = np.zeros((2, 2, 3, 2))

# With this np.full function we can define what value that need to in that elements
# With working this we need to declare that exact value as a argument, but if its not declared interpreter popup a TypeError
arr = np.full((2, 2), "Hey")

# Return a new array of given shape and type, without initializing entries.
# This means the array will contain arbitrary values (essentially, uninitialized garbage values)
arr = np.empty(2, dtype=float)
print(arr)