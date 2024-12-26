# List comprehension in Python provides a concise way to create lists

# for x in range(1, 6):
#     return x ** 2
# squares = [x ** 2 for x in range(1, 6)]

# for x in range(1, 10):
#     if x % 2 == 0:
#         return x
# even_nums = [x for x in range(1, 10) if x % 2 == 0]
# With ternary statement
# even_nums = ["even" if x % 2 == 0 else "odd" for x in range(1, 10)]
# print(even_nums)

i = 0
while i != 5:
    print(i)
    i += 1
else:
    print("Loop is completed!")