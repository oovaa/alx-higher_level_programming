#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body_content = response.read()
    utf8_content = body_content.decode('utf-8')

    print(f"\t- type: {type(body_content)}")
    print(f"\t- content: {body_content}")
    print(f"\t- utf8 content: {utf8_content}")
