marks = int(input("Enter your Marks:"))

if 0 > marks > 100:
    print("Marks is output Rang!")
elif 85 <= marks:
    print("Grade is A")
elif 75 <= marks:
    print("Grade is B")
elif 65 <= marks:
    print("Grade is C")
elif 55 <= marks:
    print("Grade is D")
else:
    print("Grade is F")