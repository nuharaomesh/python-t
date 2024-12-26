
def multiply(h):
    return lambda a : a*h

myDoubler = multiply(2)
print(myDoubler(5))

