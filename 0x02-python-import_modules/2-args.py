#!/usr/bin/python3

import sys

ls = sys.argv[1:]

for i, v in enumerate(ls):
    print("{}: {}".format(i + 1, v))
