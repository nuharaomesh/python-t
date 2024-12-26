# x = 40

# match x:
#     case 200:
#         print("Ok!")
#     case 201:
#         print("Created!")
#     case 404:
#         print("Not found!")
#     case _:
#         print("Something else")
        
number = 10

match number:
    case number % 2 == 0:
        print("Even")
    case "USER":
        print("User")
    case "user":
        print("user")
    case _:
        print("Something else!")