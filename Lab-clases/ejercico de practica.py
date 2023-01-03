# Crear matrices
import random
n = 2
matriz_a = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
matriz_b = [[random.randint(1, 10) for j in range(n)] for i in range(n)]

# Inicializar matriz resultado
resultado = [[0, 0], [0, 0]]

# Iterar a través de las filas de la matriz A
for i in range(len(matriz_a)):
   # Iterar a través de las columnas de la matriz B
   for j in range(len(matriz_b[0])):
       # Iterar a través de las filas de la matriz B
       for k in range(len(matriz_b)):
           # Realizar la multiplicación y suma de elementos de la matriz A y B y almacenar el resultado en la matriz resultado
           resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

print(resultado)
