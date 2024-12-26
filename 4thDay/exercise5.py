temperature = [20, 30, 25, 40, 50]

def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32

result = map(celsius_to_fahrenheit, temperature)
print(list(result))