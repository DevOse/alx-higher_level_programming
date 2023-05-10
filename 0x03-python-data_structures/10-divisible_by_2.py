#!/usr/bin/python3

# Function that inds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    n_list = my_list.copy()
    for num in my_list:
        if n_list[num] % 2 == 0:
            n_list[num] = 1
        else:
            n_list[num] = 0
    return n_list
