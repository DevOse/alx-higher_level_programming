#!/usr/bin/python3

# Function that prints all integers of a list in reverse

def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for num in new_list:
        print("{:d}".format(num))
