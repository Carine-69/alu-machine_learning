#!/usr/bin/env python3

"""
This module provides a function to compute the transpose of a 2D matrix
without using any external libraries.

A transpose operation converts all rows of a matrix into columns and vice versa.
"""


def matrix_transpose(matrix):
 """
    Transposes a given 2D matrix (list of lists).

    The transpose of a matrix is obtained by switching its rows with its columns.
    For a matrix of size m x n, the result will be a matrix of size n x m.

    Parameters:
    matrix (list of list of numbers): The matrix to transpose. It should be
    rectangular (i.e., all rows should have the same number of elements).

    Returns:
    list of list of numbers: A new transposed matrix.

    
    """


    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for a in range(len(matrix)):

            row.append(matrix[a][i])
        transposed.append(row)
    return (transposed)
