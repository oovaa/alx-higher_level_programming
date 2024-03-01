"""# Write a Python script that fetches
# https://alx-intranet.hbtn.io/status
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'

    data = {"q": q}

    re = requests.post(url, data=data)

    try:
        js = re.json()
        if js:
            print(f"[{js['id']}] {js['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
