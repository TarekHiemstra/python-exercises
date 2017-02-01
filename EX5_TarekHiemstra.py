# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 5: Loops
# 01 February 2017


def assignment_5(my_list):
    total = 0
    numeric_items = ["<class 'int'>", "class 'long'",
                     "class 'float'", "class 'complex'"]
    for items in my_list:
        if isinstance(items, int) == False and isinstance(items, float) == False and isinstance(items, complex) == False:
            return 0
        elif items == 0:
            break
        total += items
    return total

# PS: numeric value 'long' does not exist anymore in Python 3.
