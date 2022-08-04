#!/usr/bin/python3
""" A module that rotates 2d matrix """


def rotate_2d_matrix(matrix):
    """ A function that rotates matrix clock wise 90 degree"""
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix
