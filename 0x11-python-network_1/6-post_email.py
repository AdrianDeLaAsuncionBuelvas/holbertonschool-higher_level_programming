#!/usr/bin/python3
"""sends a POST with request Module"""
import requests
import sys

if __name__ == '__main__':
    """sends a POST request to the passed URL with email as a parameter"""
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    req = requests.post(url, data=payload)
    print(req.text)
