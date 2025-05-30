#!/usr/bin/env python3
"""
module that calculate the
 determnant of the mtrix
"""

def determinant(matrix):
    """
    first we check raise errors
      in case of invalid input
    if not list of list

    errors:

    TypeError: input must be a list of lists
    TypeError: matrix is not square
     otherwise matrix determinant is
       calulated in int or float
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row,list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if matrix == [[]]:
        return 1
    
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    
    n= len(matrix)

    if n == 1:
        return matrix[0][0]
    
    if n ==2:
        return matrix[0][0] * matrix[1][0]
    
    det = 0
    for c in range(n):
         det = np.linalg.det(np.array(matrix))
