#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

Write a Python script that takes 2 arguments
in order to solve this challenge.
"""

import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <user> <repository>")
        sys.exit(1)

    user = sys.argv[1]
    repos = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repos}/commits'

    response = requests.get(url)
    response.raise_for_status()
    commits = response.json()

    for commit in commits[:10]:
        name = commit.get('commit').get('author').get('name')
        sha = (commit.get('sha'))
        print(f"{sha}: {name}")
