#!/usr/bin/python3
"""urllib Python fetches Module"""
import urllib.request

if __name__ == '__main__':
    """Python script that fetches"""
    url = 'https://intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
