#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    add_numerator = 0
    add_denominator = 0
    for elem in my_list:
        add_numerator += elem[0] * elem[1]
        add_denominator += elem[1]
    return add_numerator / add_denominator
