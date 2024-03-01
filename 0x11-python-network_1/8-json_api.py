#!/usr/bin/python3
# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status
import requests
import sys

q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'

data = {"q": q}

re = requests.post(url, data=data)

js = re.json()
if js:
    print(f"[{js['id']}] {js['name']}")
else:
    print("No result")
