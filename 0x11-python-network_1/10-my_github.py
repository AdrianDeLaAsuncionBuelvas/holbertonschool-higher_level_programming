#!/usr/bin/python3
"""Github API module"""
import requests
import sys

if __name__ == '__main__':
    """script that takes your Github credentials user, passwd"""
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        url = 'https://api.github.com/user'
        req = requests.get(url, auth=(username, password))
        R_json = req.json()
        print(R_json.get('id'))
    except:
        print("None")
