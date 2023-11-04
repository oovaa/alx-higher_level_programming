#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return [x for x in my_list]

    lis = [element if i == idx else x for i, x in enumerate(my_list)]
    return lis
