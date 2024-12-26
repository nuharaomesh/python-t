
my_sports = ("cricket", "tennis", "football")

converted_tuple = list(my_sports)

print(type(converted_tuple))

converted_tuple[1] = "hockey"
my_sports = tuple(converted_tuple)

print(my_sports, type(my_sports))