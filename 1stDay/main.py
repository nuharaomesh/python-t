# a = 2000

# print("Type of variable having value", a, "is", type(a))

# num_1 = 2.5e4
# print(num_1)
# print(type(num_1))


# num_1 = 5
# new_num = float(num_1)
# print(new_num)
# print(type(new_num))

# num_2 = 10.2
# new_num_2 = int(num_2)
# print(new_num_2)
# print(type(new_num_2))

# print(type(my_list))

# my_list[1] = 33

# print(my_list)
# print(len(my_list))

# print(my_list[-2])

# print(my_list[3])

# my_list[2], my_list[3] = "Dog", 19.0

# my_list.insert(3, "Omesh")
# my_list.append("kamal")

# new_list = ["bus", False, 17]
# my_list.extend(new_list)
# print(my_list, len(my_list))


# my_list.pop(2) remove a value giving the index value


# del my_list[1]

# my_list.clear()
# my_list.sort(reverse=True)
# my_list_2.sort(key=str.lower)

# my_list = [1, 10, 10, 2, 8, 5]
# my_list_2 = ["dog", "parrot", "apple", "Duck", "Cat", "racoon"]

# my_list_2.reverse()

# print(my_list_2)
# print(my_list, len(my_list))

numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print("Sum of elements:", total)
print(numbers)
for x in numbers:
    numbers.insert(0, numbers[len(numbers) - 1])
    numbers.pop()
    print(numbers)

# for number in numbers:
#     numbers.insert(0, numbers[len(numbers) - 1])
#     print(numbers)