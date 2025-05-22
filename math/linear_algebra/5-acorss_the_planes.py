#!/usr/bin/env python3
"""
This module defines a function to add two 2D matrices element-wise.

The function returns a new matrix with summed elements if both matrices
are the same shape. If not, it returns None.
"""

def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None

    result = []
    for i in range(len(mat1)):
        row = []
        for a in range(len(mat1[0])):
            row.append(mat1[i][a] + mat2[i][a])
        result.append(row)
    return result


# Example usage
mat1 = [[2, 3, 1], [4, 5, 6], [9, 8, 7]]
mat2 = [[9, 8, 7], [4, 5, 6], [1, 2, 3]]

result = add_matrices2D(mat1, mat2)
print(result)
