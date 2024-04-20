"""Module `task_02` provides function `get_numbers_ticket(min, max, quantity)` that allows to calculate
set of unique numbers in range from `min` to `max` with quantity `quantity`."""

import random

def get_numbers_ticket(min, max, quantity):
    """Calculates set of unique numbers in range from `min` to `max` with quantity `quantity`."""
    try:
        if min > max:
            raise ValueError("Min number should be less or equal to max number.")
        if quantity > max+1 - min:
            raise ValueError(
                "Quantity of numbers should be less or equal to diff between max and min numbers.")
        return random.sample(range(min, max+1), quantity)
    except ValueError as e:
        print(f"Error: {e}")
        return []


# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Your lottery numbers:", lottery_numbers)

min = int(input("Enter min number: "))
max = int(input("Enter max number: "))
quantity = int(input("Enter quantity of numbers: "))
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Your lottery numbers:", lottery_numbers)
