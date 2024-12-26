
my_sports = ("cricket", "tennis", "football")

print(my_sports)
print(type(my_sports))
print("Length is:", len(my_sports))

new_tuple = ("Omesh",) # after define a tuple with single value we need to add a comma , after the value. if it's not python interpreter get this one as a str

print(type(new_tuple))

# my_sports[0] = "asd" 
# We cannot change the value in tuples

converted_tuple = list(my_sports)

print(type(converted_tuple))

converted_tuple[1] = "hockey"
my_sports = tuple(converted_tuple)

print(my_sports, type(my_sports))