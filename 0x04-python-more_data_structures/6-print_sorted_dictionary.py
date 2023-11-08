#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for v in sorted(a_dictionary):
        print("{}: {}".format(v, a_dictionary.get(v)))
