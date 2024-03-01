#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':

    user = sys.argv[1]
    tok = sys.argv[2]

    url = f'https://api.github.com/users/{user}'

    # Make a GET request to the GitHub API
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, tok))

    # Print the user id
    print(response.json().get('id'))
