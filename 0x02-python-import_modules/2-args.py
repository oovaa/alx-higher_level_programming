#!/usr/bin/python3

import sys

ls = sys.argv[1:]

if len(ls) == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(len(ls)))


for i, v in enumerate(ls):
    print("{}: {}".format(i + 1, v))
