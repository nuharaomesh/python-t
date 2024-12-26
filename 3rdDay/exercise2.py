
x = -2

match x:
    case 0:
        print("Zero")
    case -1:
        print("Negative one")
    case 1:
        print("Positive one")
    case x if x > 1:
        print("Positive number greater than one")
    case _ if x < -1:
        print("Negative number less than negative one")
    case _:
        print("Unmatched case")