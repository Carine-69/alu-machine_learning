#!/usr/bin/env python3
def inverse(matrix):
   if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
   if any(len(row) != len(matrix) for row in matrix):
    raise TypeError("matrix must be a square matrix")
    if matrix == [[]]:
      return(1)

   return(np.linalg.det(np.array(matrix)))
