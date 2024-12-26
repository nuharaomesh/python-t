
# def arbitrary_keyword_argument(**kwargs):
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(f"{key} = {value}")
    
# arbitrary_keyword_argument(name="Omesh", age=21)

def kwargs(**args):
    string = ""
    for key,value in args.items():
        string += f"{key} = {value},"
    string
    return string 

print(kwargs(name="Omesh", age=22))