#!/usr/bin/python3
"""# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import requests
    import sys
    re = requests.get(sys.argv[1])
    print(re.headers.get('X-Request-Id'))
