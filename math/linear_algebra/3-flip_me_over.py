#!/usr/bin/env python3
def transpose(matrix):
  matrix_transpose = []
  for i in range (len(matrix[0])):
    row = []
    for a in range(len(matrix)):

      row.append(matrix[a][i])
      matrix_transpose.append(row)
  return(matrix_transpose)
