my_tuple_1 = (10, 8, 20, 5)
my_tuple_2 = (5, 9, -1)

converted_tuple_1 = list(my_tuple_1)
converted_tuple_2 = list(my_tuple_2)

converted_tuple_1.pop(2)
join_list = converted_tuple_1 + converted_tuple_2
join_list.sort()

join_tuple = tuple(join_list)

print(join_tuple) 