#!/usr/bin/python3
""" In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n what is Minimum Operations
    to get n characters
"""


def minOperations(n):
    """
    a function that calculates the fewest number of operations
    needed to result in exactly n H characters in the file

    args:
        n: NUmber of charters to be displayed

    return:
          number of minimum operation
    """
    curr = 1
    prev = 0
    count = 0

    while (curr < n):
        empty_position = n - curr

        if (empty_position % curr == 0):
            prev = curr
            curr += prev
            count += 2
        else:
            curr += prev
            count += 1
    return count
