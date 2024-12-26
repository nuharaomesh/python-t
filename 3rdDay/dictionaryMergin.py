
my_dict_1 = {
    "Name": "Omesh"
}

my_dict_2 = {
    "Age": 22
}

my_dict_3 = my_dict_1 | my_dict_2
# print(my_dict_3)

# print(my_dict_3["Name"])
print(my_dict_3.get("Name", ""))
print(my_dict_3.get("address", "Not found"))