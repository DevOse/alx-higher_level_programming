#!/usr/bin/python3

# Function that inds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    n_list = my_list.copy()
    for num in range len(my_list):
        if n_list[num] % 2 == 0:
            n_list[num] = True
        else:
            n_list[num] = False
    return n_list
