#!/usr/bin/python3
# Function that adds two tuples

def add_tuple(tuple_a=(), tuple_b=()):
    tupA = tuple_a + (0, 0)  # pads tuple_a with zeros if smaller than 2
    tupB = tuple_b + (0, 0)  # pads tuple_ with zeros if smaller than 2
    
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
