def sum_diagonal(A):
  # Verificamos que la matriz sea cuadrada
  if len(A) != len(A[0]):
    raise ValueError("La matriz debe ser cuadrada para tener una diagonal principal")

  # Calculamos la suma de la diagonal principal
  diagonal_sum = 0
  for i in range(len(A)):
    diagonal_sum += A[i][i]

  return diagonal_sum
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_sum = sum_diagonal(A)

print(f"La diagonal de matriz es:\n{diagonal_sum}") 
