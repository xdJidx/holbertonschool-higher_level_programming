#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()

    for num in my_list:
        unique_nums.add(num)

    sum_unique = sum(unique_nums)

    return sum_unique
