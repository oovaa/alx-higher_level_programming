# 0x11-python-network_1

This project is part of Holberton School curriculum. In this project, we will be exploring networking in Python.

## Description

This repository contains various scripts that demonstrate the use of Python for network programming. It covers topics such as sending HTTP requests, handling HTTP responses, and working with JSON data.

## Files

Here are the Python scripts in this repository:

* `0-hbtn_status.py`: Script that fetches https://intranet.hbtn.io/status
* `1-hbtn_header.py`: Script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
* `2-post_email.py`: Script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.
* `3-error_code.py`: Script that takes in a URL, sends a request to the URL and displays the body of the response, managing HTTP error exceptions.
* `4-hbtn_json.py`: Script that sends a request to a URL and displays the body of the response, managing JSON format.
* `5-hbtn_response_header.py`: Script that takes in a URL, sends a request to the URL and displays the value of a variable in the response header.

## Usage

Each script starts with a shebang that points to the python3 interpreter. To run, use:
```bash
./script_name.py