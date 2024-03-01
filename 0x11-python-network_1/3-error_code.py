#!/usr/bin/python3
# Write a Python script that takes in a URL,
# sends a request to the URL and displays the body
# of the response (decoded in utf-8).
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            body_content = res.read()
            utf8_content = body_content.decode('utf-8')
            print(utf8_content)
    except HTTPError as e:
        print("Error code:", e.code)
