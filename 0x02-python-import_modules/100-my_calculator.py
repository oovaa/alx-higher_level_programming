#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    ls = sys.argv[1:]

    if len(ls) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(ls[0])
    b = int(ls[2])

    if ls[1] == "+":
        re = add(a, b)
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "-":
        re = sub(a, b)
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "*":
        re = mul(a, b)
        print("{} {} {} = {}".format(a, ls[1], b, re))

    elif ls[1] == "/":
        re = div(a, b)
        print("{} {} {} = {}".format(a, ls[1], b, re))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
