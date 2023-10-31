#!/usr/bin/python3

for i in range(0, 90):
    if i % 10 > i // 10:
        print("{}".format(i), end=" "if i != 89 else "\n")
