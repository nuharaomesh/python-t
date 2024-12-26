
number = [4]6

match number:
    case [x]:
        print(x)
    case [x, y]:
        print(x * y)
    case [x, y, z]:
        print(x + y + z)
    case _:
        print("The list does not contain 2 or 3 numbers")