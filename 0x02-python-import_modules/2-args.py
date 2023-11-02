#!/usr/bin/python3

import sys

ls = sys.argv[1:]

num_args = len(ls)

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

for i, v in enumerate(ls):
    print("{}: {}".format(i + 1, v))
