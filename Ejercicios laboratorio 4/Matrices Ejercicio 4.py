def transpose_matrix(A):
  # Creamos la matriz transpuesta con el número de filas y columnas invertidos
  T = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]

  # Copiamos los elementos de A a T, cambiando filas por columnas
  for i in range(len(A)):
    for j in range(len(A[0])):
      T[j][i] = A[i][j]

  return T
A = [[1, 2, 3], [4, 5, 6]]
T = transpose_matrix(A)
print(f"La transpuesta de la matriz:\n{T}")