def sum(x, y):
    return x + y

list_1 = [1, 2, 33, 42]
list_2 = [1, 2, 33, 42]

output = map(sum, list_1, list_2)
print(list(output))