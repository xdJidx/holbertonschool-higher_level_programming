#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for key in sorted_list:
        print("{}: {}".format(key, a_dictionary[key]))
