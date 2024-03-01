#!/usr/bin/python3
"""# Write a Python script that takes in a URL and an email,
# sends a POST request to the passed URL with the email as a parameter,
# and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    en_data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(url, en_data)

    with urllib.request.urlopen(request) as res:
        # Read and decode the response content
        result = res.read().decode('utf-8')
        print(result)
