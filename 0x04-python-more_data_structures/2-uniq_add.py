#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for elem in set(my_list):
        add = elem + add
    return (add)