#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    ls = sys.argv[1:]

    if len(ls) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(ls[0])
    b = int(ls[2])

    if ls[1] == "+":
        re = a + b
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "-":
        re = a - b
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "*":
        re = a * b
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "/":
        re = a / b
        print("{} {} {} = {}".format(a, ls[1], b, re))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
