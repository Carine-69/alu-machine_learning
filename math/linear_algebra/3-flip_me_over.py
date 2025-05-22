#!/usr/bin/env python3
def transpose(matrix):
  transposed = []
  for i in range (len(matrix[0])):
    row = []
    for a in range(len(matrix)):

      row.append(matrix[a][i])
      transposed.append(row)
  return(transposed)
