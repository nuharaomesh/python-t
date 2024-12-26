target_number = 6
num_list = [1, 2, 3, 4, 5]

i = 0
for x in num_list:
    for z in num_list:
        sum = x + z
        if sum == target_number:
            print("Sum:", sum)
            print("Pairs: (", x,",", z, ")")
        