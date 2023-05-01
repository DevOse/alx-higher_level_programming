#!/usr/bin/python3

# Function that prints all integers of a list in reverse

def print_reversed_list_integer(my_list=[]):
    for num in (my_list[::-1]):
        print("{:d}".format(num))
