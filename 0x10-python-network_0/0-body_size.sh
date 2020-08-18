#!/bin/bash
# Write a Bash script that takes in a URL.
curl -s -I "$1" | grep Content-Length | cut -d' ' -f2
