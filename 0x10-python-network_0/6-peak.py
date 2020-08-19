#!/usr/bin/python3
"""Find Peak Function Module"""


def find_peak(list_of_integer):
    """function that finds a peak in a list of unsorted integers"""
    if not list_of_integer:
        return (None)
    return R_fp(list_of_integer, 0, len(list_of_integer) - 1,
                len(list_of_integer))


def R_fp(arr, low, high, num):
    """function complement"""
    part = low + (high - low)//2

    if (part == 0 or arr[part-1] <= arr[part]) and \
       (part == num - 1 or arr[part+1] <= arr[part]):
        return (arr[part])
    elif part > 0 and arr[part-1] > arr[part]:
        return (R_fp(arr, low, part - 1, num))
    else:
        return (R_fp(arr, part + 1, high, num))
