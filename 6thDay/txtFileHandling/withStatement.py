# With statement no need for file.close() manually call this close function after operation is done it automatically closed
# with open("6thDay/txtFileHandling/eample.txt") as file:
    # print(type(file))
    
# Writing in files with with statement
# with open("6thDay/txtFileHandling/example.txt", 'w') as file:
#     file.write("Hello there\nIm omesh")

# Writing in files with writelines() function
# In this we need to declare a list that hold text lines as elements
# with open("6thDay/txtFileHandling/example.txt", 'w') as file:
#     text = ["Hello there!!\n", "Im omesh"]
#     file.writelines(text)


# Append data to an existing file
# with open("6thDay/txtFileHandling/example.txt", 'a') as file:
    # same as in write mode 'w' write() function is also available for this append mode 'a'
    # file.write("\nsdfdsfd")
    # same as 'w' mode 
    # text = ["Hello there!!\n", "Im omesh\n"]
    # file.writelines(text)
    
with open("6thDay/txtFileHandling/example.txt", 'w+') as file:
    # Also write function return the characters count that hold in the write function
    t = file.write("asdasdasd\nasdasd")
    print(t)