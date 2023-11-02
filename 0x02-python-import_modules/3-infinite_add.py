#!/usr/bin/python3
import sys

sum = 0
lis = sys.argv[1:]

for i in lis:
    sum += int(i)

print("{}".format(sum))
