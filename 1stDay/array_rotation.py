number_arr = [10, 20, 30, 40, 50]

print(number_arr)

for numbers in number_arr:
    number_arr.insert(0, number_arr[len(number_arr) - 1])
    number_arr.pop()
    print(number_arr)