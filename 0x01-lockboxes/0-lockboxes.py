#!/usr/bin/python3

""" A module for lockboxes task"""


def join(T, R):
    """ A function that appends to a list"""
    res = []
    for e in R:
        res += T[e]
    return res


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True

    return len(total) == len(boxes)
