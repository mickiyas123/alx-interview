#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle

    arguments
             n: mumber of pascal triangle a user wants
    """
    output = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    output[i].append(1)
                else:
                    output[i].append(output[i - 1][j - 1] + output[i - 1][j])
            elif (j == i):
                output[i].append(1)
    return output
