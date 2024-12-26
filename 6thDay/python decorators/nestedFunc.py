# def outer(num_1):
#     # Inner function
#     def inner(num_2):
#         return num_1 + num_2
#     return inner

# # Set the parameter to the outer function and that function return the inner function
# # So we can get the return type and call the inner function 
# add_two = outer(5)
# sum = add_two(4)
# print(sum)

# Pass function as Argument
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def calculate(func, x, y):
#     return func(x, y)

# add_number = calculate(add, 5, 2)
# subtract_number = calculate(subtract, 5, 2)

# print(add_number)
# print(subtract_number)

# Return function as a value
# def greeting(name):
#     def hello():
#         return "Hello " + name + "!"
#     return hello

# greet = greeting("Omesh")
# print(greet())

# def hello(func):
#     def inner():
#         print("I got decorated!")
#         func()
#     return inner


# Instead of assigning the function call to a variable, Python provides a much more elegant way to achieve this functionality using the @ symbol. For example    
# decorated_func = make_pretty(ordinary)
# decorated_func()

# @hello
# def ordinary():
#     print("Im ordinary")
# ordinary()

def check(func):
    def inner(a, b):
        print(f"Going to divide {a} and {b}")
        if b == 0:
            print("Do not assign 0 as second value!")
        else:
            print(func(a, b))
    return inner
            
@check
def divide(a, b):
    return a/b

divide(1, 0)
