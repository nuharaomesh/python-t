def employee_info(name, **info):
    print("Employee name is:", name)
    
    for key,value in info.items():
        print(f"{key}:{value}")
    
    return {"Name":name} | info

print(employee_info("Omesh", age=22, role="dev"))