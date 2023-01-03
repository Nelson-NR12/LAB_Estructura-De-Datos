#Para determianr si una matriz es simetrica debemos tener una propia matriz transpuesta
def matriz_simet(matrix):
  return matrix == list(map(list, zip(*matrix)))

matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(matriz_simet(matriz))  # Output: True

matrix = [[1, 2, 3], [4, 5, 6]]
print(matriz_simet(matriz))  # Output: False
