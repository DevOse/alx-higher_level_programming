#!/usr/bin/python3
# Function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max = my_list[0]  # Initialize the max value to the first element of the list
    for num in my_list:  # Iterate over the rest of the list
        if max <= num:
           max = num
    return max
