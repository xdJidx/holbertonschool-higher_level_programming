#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    lengList = len(my_list)
    if idx > lengList:
        return None
    return my_list[idx]
