#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    lis = [element if i == idx else x for i, x in enumerate(my_list)]
    return lis
