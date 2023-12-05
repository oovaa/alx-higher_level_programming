#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w",) as f:
        f.write(json.dumps(my_obj))
