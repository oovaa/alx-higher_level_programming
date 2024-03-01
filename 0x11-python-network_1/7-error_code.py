#!/usr/bin/python3
"""# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    re = requests.get(url)

    if re.status_code >= 400:
        print('Error code:', re.status_code)

    else:
        print(re.text)
