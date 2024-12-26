
def calculate_total_cost(item_price, qty, discount = 0, tax = 0):
    total = item_price * qty
    new_total = total * discount / 100
    return 

print(calculate_total_cost(1000, 10, 10, 1))
    