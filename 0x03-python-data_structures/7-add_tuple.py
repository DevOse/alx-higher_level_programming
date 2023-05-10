#!/usr/bin/python3
# Function that adds two tuples

def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    # check conditions for A
    if lenA < 1:
        tuple_a = (0, 0)
    elif lenA < 2:
        tuple_a = (tuple_a[0], 0)
    elif lenA > 2:
        tuple_a = (tuple_a[0], tuple_a[1])

    # check conditions for B
    if lenB < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)
    elif lenB > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    sums = tuple(map(sum, zip(tuple_a, tuple_b)))
    return (sums)

# tuple_a = 1, 89
# tuple_b = 88, 11
# new_tup = add_tuple(tuple_a, tuple_b)
# print(new_tup)
# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
