import json

passed_students = []
json_file_path = "6thDay/exercise/records.json"

with open(json_file_path) as json_file:
    json_data = json.load(json_file)
    # print(type(json_data))
    
    for student in json_data:
        
        total_grades = 0
        
        grades = student["student_grades"]
        
        for key,value in grades.items():
            total_grades += value
            
        if total_grades >= 75:
            passed_students.append(student)


with open("6thDay/exercise/passed_students.json", "w") as json_file:
    json_data = json.dumps(passed_students)
    json_file.write(json_data)