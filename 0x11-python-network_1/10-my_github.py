#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""
from sys import argv
import requests

if __name__ == '__main__':

    user = argv[1]
    tok = argv[2]

    url = f'https://api.github.com/users/{user}'

    # Make a GET request to the GitHub API
    response = requests.get(url, auth=(user, tok))

    # Print the user id
    print(response.json().get('id'))