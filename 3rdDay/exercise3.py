my_list = []


match my_list:
    case []:
        print("Empty list")
    case [x]:
        print("List has single element")
    case [x, y]:
        print("Lists has two elements")
    case _:
        print("This is something else")