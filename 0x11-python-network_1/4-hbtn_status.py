#!/usr/bin/python3
"""Requests Module"""
import requests

if __name__ == "__main__":
    """script that fetches with Resquests"""
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
