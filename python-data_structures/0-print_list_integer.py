#!/usr/bin/python3
def print_list_integer(my_list=[]):
    lengList = len(my_list)
    index = 0
    while index < lengList:
        print("{:d}".format(my_list[index]))
        index += 1
