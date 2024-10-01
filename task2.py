import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000) or not (1 <= max <= 1000) or not (min <= max):
        return []
    
    if quantity > (max - min + 1):
        return []
    numbers = random.sample(range(min, max+1), quantity)
    return sorted(numbers)
    
print(get_numbers_ticket(10, 50, 5))