#!/usr/bin/python3
"""Request value X-Request-Id with requests Module"""
import requests
import sys

if __name__ == '__main__':
    """displays the value of the variable X-Request-Id"""
    url = sys.argv[1]
    R = 'X-Request-Id'
    req = requests.get(url)

    print(req.headers.get(R))
