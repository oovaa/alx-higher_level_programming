#!/usr/bin/python3
# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {"email", email}

re = requests.post(url, data=data)
