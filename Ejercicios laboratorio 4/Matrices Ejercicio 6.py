import numpy as np

def det_matriz_a(matrix, i, j):
  return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def det_matriz(matrix):
  # caso de matriz 3x3
  if len(matrix) == 2 and len(matrix[0]) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

  determinante = 0
  for c in range(len(matrix)):
    determinante += ((-1)**c) * matrix[0][c] * det_matriz(det_matriz_a(matrix, 0, c))
  return determinante

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(det_matriz(matrix))  

matrix = [[1, 0, 2], [0, 5, 0], [2, 0, 3]]
print(det_matriz(matrix))  
