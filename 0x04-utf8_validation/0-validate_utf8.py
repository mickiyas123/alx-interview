#!/usr/bin/python3
"""  A module that checks if a data is utf8 valid"""


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    for num in data:
        if num >= 256:
            return False
    return True
