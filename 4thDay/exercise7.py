people = [("Omesh", 22), ("Nuhara", 17), ("ALice", 31)]

result = filter(lambda person : person[1] >= 18, people)
print(list(result))