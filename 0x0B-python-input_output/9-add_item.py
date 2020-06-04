#!/usr/bin/python3

"""
adds all arguments to a Python list, \
and then save them to a file
"""
import json
import sys
import os


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
"""check if the file is in the path"""
exists = os.path.isfile(filename)

"""
check if the file exists
"""
if exists:
    my_list = load_from_json_file(filename)
else:
    my_list = []

"""
if more than one argument is entered add it, \
but leave the list empty
"""
for ac in sys.argv:
    if ac == "./9-add_item.py":
        continue
    my_list.append(ac)

save_to_json_file(my_list, filename)
