import numpy as np
matrizA = np.array([[1,2,3],[4,5,6],[7,8,9]], float)
matrizB = np.array([[9,8,7],[6,5,4],[3,2,1]], float)

suma = matrizA + matrizB
resta = matrizA - matrizB
multiplicacion = matrizA*matrizB
print(f"Suma de matrices: \n{suma} \n\n Resta de Matrices: \n{resta} \n\n Multiplicación de matrices \n{multiplicacion}")
