
def calculate_sum(num_1, num_2):
    return num_1 + num_2

result = map(calculate_sum, [1, 2, 3], [1, 2, 3])

print(list(result))