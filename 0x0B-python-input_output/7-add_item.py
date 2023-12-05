#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

from sys import argv
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fn = "add_item.json"

try:
    cur = load_from_json_file(fn)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    cur = []

argv = argv[1:]

full = cur + argv

save_to_json_file(full, fn)
