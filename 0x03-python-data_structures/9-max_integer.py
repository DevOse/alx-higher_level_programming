#!/usr/bin/python3
# Function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = 0
    for num in my_list:
        if num > max:
            max = num
    return max
