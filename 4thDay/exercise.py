
def calculate(*param):
    sum = 0
    for x in param:
        sum += x
    return sum

print(calculate(1, 2, 3))