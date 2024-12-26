
def summarite_grades(name, *grades):
    
    if not grades:
        print("No grades available!")
        
    print("Student name:", name)
    print(name, "Maximum grade is", max(*grades))
    print(name, "Minimum grade is", min(*grades))
    print(name, sum(*grades) / len(*grades))
    
summarite_grades("omesh", (3, 22, 1,))