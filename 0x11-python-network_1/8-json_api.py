#!/usr/bin/python3
"""requests with JSON Module"""
import requests
import sys

if __name__ == '__main__':
    """Sends a POST requests to URL with the letter as a parameter"""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = {'q': sys.argv[1]}
        req = requests.post(url, data=q)
        if req.headers.get('content-type') != 'application/json':
            raise TypeError
        if req.json():
            print("[{}] {}".format(req.json()['id'], req.json()['name']))
        else:
            print("No result")
    except IndexError:
        print("No result")
    except TypeError:
        print("Not a valid JSON")
