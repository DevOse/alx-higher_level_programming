#!/usr/bin/python3

# Function that prints all integers of a list in reverse

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))
