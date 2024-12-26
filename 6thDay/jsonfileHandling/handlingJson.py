# to working with json, we need to import json module
import json

# with open("6thDay/jsonfileHandling/person.json", 'r') as file:
#     # json.load('file') this load functions functionality is converting json into dictionary
#     json_content = json.load(file)
#     print(json_content)

data = {
    "name": "Omesh",
    "age": 22,
    "address": "Colombo"
}

json_file_path = "6thDay/jsonfileHandling/paerson.json" 

with open(json_file_path, 'r+') as file:
    #first of all we need to convert python data structure to a json type
    json_file = json.load(file)
    print(json_file)
    json_data = json.dumps(data, indent=3)
    print(json_data)
    # writing in the json file with write function (same as txt file handling write() function)
    file.write(json_data)