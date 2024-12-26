# Same as working with json files we need to import csv module for csv files operations
import csv

# Reading csv
csv_file_path = "6thDay/csvFileHandling/People.csv"
# with open(csv_file_path, mode='r', newline='') as file:
#     # with csv.DictReader(file) function we can read the csv files
#     # After reading opr, this func return the csv file rows as python dictionaries
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Printing row dictionaries
#         print(row)

# Writing in csv

# # Csv file row data
data = [
    {"Name": "Omesh", "Age": 45, "Address": "Galle"},
    {"Name": "Nuhara", "Age": 12, "Address": "Colombo"},
    {"Name": "Kamal", "Age": 25, "Address": "Colombia"}
]
# Column names
field_names = ["Name", "Age", "Address"]

with open(csv_file_path, mode='w', newline='') as file:
    
    # Writing csv file data with csv.DictWriter(file, fieldnames=field_names) function 
    # In this function we need to define file and fieldnames
    csv_writer = csv.DictWriter(file, fieldnames=field_names)
    
    # After getting instance from that function we can call writeheader() func for creating headers
    csv_writer.writeheader()
        
    # For inserting row data we need to iterate declared dictionary list
    for row in data:
        # Inserting row data in the csv file with writerow() func
        csv_writer.writerow(row)

# Manipulating csv data
adult_people = []

with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    # Fetching csv data rows one by one
    for row in reader:
        # check the adult person with age
        if int(row["Age"]) > 18:
            # Add to the new list one by one
            adult_people.append(row)
        
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    
    # for row in adult_people:
    #     # Inserting adult people to the csv file
    #     writer.writerow(row)
    
    # Instead of inserting single row one at a time we can insert whole list with writerows() function
    writer.writerows(adult_people)