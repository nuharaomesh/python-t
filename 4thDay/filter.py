my_list = [1, 2 , 33, 53, 23, 24, 12]

def filter_max(num):
    return num > 10

result = filter(filter_max, my_list)

print(list(result))