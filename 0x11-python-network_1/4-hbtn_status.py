#!/usr/bin/python3
"""# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    re = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type:", type(re.text))
    print("\t- content:", re.text)
