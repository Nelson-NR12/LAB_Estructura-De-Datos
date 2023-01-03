#Multiplicación de matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

def multi_matrices(A, B):
  # Verificamos que el número de columnas de A sea igual al número de filas de B
  if len(A[0]) != len(B):
    raise ValueError("El número de columnas de A debe ser igual al número de filas de B para poder multiplicar las matrices")

  # Creamos la matriz resultado con el número de filas de A y el número de columnas de B
  C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

  # Multiplicamos elemento a elemento
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j]

  return C
C = multi_matrices(A, B)
print(f"La multiplicación de matrices:\n{C}") 