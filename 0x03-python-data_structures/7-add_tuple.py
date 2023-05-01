#!/usr/bin/python3
# Function that adds two tuples

def add_tuple(tuple_a=(), tuple_b=()):
    list_1 = []

    tuple_c = zip(tuple_a, tuple_b)   # Pairs the 2 tuples together
    for tups in tuple_c:
        list_1.append(sum(tups))
    return (tuple(list_1))
