#!/usr/bin/python3

def uppercase(str):
    re = ''.join(chr(ord(char) - 32) if char.islower()
                 else char for char in str)
    print(re)

# for i in range(len(s)):
#     if s[i].islower():
#        s[i] = chr(ord(s[i]) - 32)

# re = ''.join(s)
# re = ''.join(chr(ord(char) - 32) if char.islower() else char for char in s)

# print(re)
