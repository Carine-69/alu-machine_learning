#!/usr/bin/env python3
"""
module for returning the shape 
or dimension of any given matrix
"""
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
