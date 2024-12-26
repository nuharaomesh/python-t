
# def find_factorial(n):
#     fact = 1
#     for x in range(1,n + 1):
#         fact *= x
#     return fact
        
# print(find_factorial(5))

def find_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * find_factorial(x - 1))
    
print(find_factorial(1001))