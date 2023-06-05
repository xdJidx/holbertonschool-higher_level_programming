#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))  # Add zeros if tuple_a has less than 2 elements
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))  # Add zeros if tuple_b has less than 2 elements

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
