#!/usr/bin/python3
# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status
import requests
import sys

if __name__ == '__main__':
    re = requests.get(sys.argv[1])
    print(re.headers.get('X-Request-Id'))
