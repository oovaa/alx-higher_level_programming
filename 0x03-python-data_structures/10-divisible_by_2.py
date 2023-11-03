#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    tof = []
    for i in my_list:
        if i % 2 == 0:
            tof.append(True)
        else:
            tof.append(False)
    return tof
