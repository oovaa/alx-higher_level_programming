#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    mx = my_list[0]
    for i in my_list[1:]:
        if mx < i:
            mx = i
    return mx
