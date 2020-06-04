#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of \
integers representing the Pascal’s triangle of n
    """
    list_res = []
    if n <= 0:
        return (list_res)
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(list_res[-1][j:j + 2]))
        list_res.append(row)
    return (list_res)
