my_list = [1, 2, 3, 4, 5]

def calculate_sum(lst):
    if not lst:
        return 0 
    return lst[0]+calculate_sum(lst[1:])
    
calculate_sum(my_list)