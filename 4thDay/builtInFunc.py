
# x = -2
# print(abs(x)) # get the absolute value


# map() function

def find_square(x):
    return x * x

result = map(find_square, [1, 2, 3])
print(type(result))
print(list(result))
