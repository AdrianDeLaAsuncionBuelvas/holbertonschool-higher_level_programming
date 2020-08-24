#!/usr/bin/python3
"""Sends a POST request module"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """sends a POST request to the passed URL with the email as a paramete"""
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode('utf-8'))
