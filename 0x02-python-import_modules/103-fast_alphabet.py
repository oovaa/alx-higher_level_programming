#!/usr/bin/python3
for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end="" if i != ord("Z") else "\n")
