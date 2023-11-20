#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])

        except (ZeroDivisionError):
            print("division by 0")
            newlist.append(0)
        except (TypeError):
            print("wrong type")
            newlist.append(0)
        except (Exception):
            newlist.append(0)

    return newlist
