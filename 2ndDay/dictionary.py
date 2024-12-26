
dict_1 = {
    "name": "Sugar",
    "price": 250.00,
    "weight": "1kg"
}

# print(dict_1, type(dict_1), len(dict_1))
# print(dict_1["weight"])

# dict_1["price"] = 10.1 # Update single items

# converted_list = list(dict_1)
# print(converted_list)

# dict_1.update({  # Update multiple items
#     "weight": "2kg",
#     "price": 220
# })

# print(dict_1)

# dict_1["color"] = "white" # add new item to the dictionary

# print(dict_1, len(dict_1))

# dict_1.pop("color") # Remove a item
# print(dict_1, len(dict_1))

# dict_1.popitem() # Removing the last item in the dictionary

# dict_1.clear() // When we need to clear the dictionary we can use the clear() method this work for all python collections

# del dict_1["price"]
# del dict_1 # Technical key is for this "Destroy" destroy the dictionary

new_dict_1 = dict_1.copy()
dict_1["weight"] = "110kg"
# print(dict_1)
# print(new_dict_1)
print(dict_1.keys())