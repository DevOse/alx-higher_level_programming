#!/usr/bin/python3
# Function that adds two tuples

def add_tuple(tuple_a=(), tuple_b=()):
    list_1 = []
    if len(tuple_a) >= 2 or len(tuple_b) >= 2:
        tuple_c = zip(tuple_a, tuple_b)   # Pairs the 2 tuples together
        for tups in tuple_c:
            list_1.append(sum(tups))
    elif len(tuple_a) < 2:
        tuple_a = (0, 0)
    elif len(tuple_b) < 2:
        tuple_b = (0, 0)
    return (tuple(list_1))
