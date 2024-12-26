my_list = [5, 7, 8, 3, 12, 14]

def filtering_odds(num):
    return num % 2 == 0

result = filter(filtering_odds, my_list)
print(list(result))
print(type(result))