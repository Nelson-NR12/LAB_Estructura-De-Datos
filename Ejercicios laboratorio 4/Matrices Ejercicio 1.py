#suma de matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

def sum_matrices(A, B):
  # Verificamos que las matrices tengan el mismo tamaño
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise ValueError("Las matrices deben tener el mismo tamaño para poder sumarse")

  # Creamos la matriz resultado con la misma dimensión que A y B
  C = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

  # Sumamos elemento a elemento
  for i in range(len(A)):
    for j in range(len(A[0])):
      C[i][j] = A[i][j] + B[i][j] #Del mismo modo se aplica el mismo criterio para la resta de matrices.
  return C
C = sum_matrices(A, B)
print(f"La suma de matrices:\n{C}")
