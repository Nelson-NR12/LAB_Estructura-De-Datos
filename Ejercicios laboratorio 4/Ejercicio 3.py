vector = []

# Leemos el vector
tamaño = int(input("Ingrese el tamaño del vector: "))
for i in range(tamaño):
  elemento = int(input(f"Ingrese el elemento {i+1}: "))
  vector.append(elemento)

# Calculamos la suma de todos los elementos del vector
total = sum(vector)

# Buscamos un elemento que sea igual a la suma de los demás elementos del vector
found = False  # Inicializamos la bandera en False
for i in range(tamaño):
  if total - vector[i] == vector[i]:
    found = True  # Cambiamos la bandera a True
    break  # Terminamos el ciclo

# Mostramos en pantalla el resultado
if found:
  print("Hay un elemento que es igual a la suma de los demás elementos del vector")
else:
  print("No hay ningún elemento que sea igual a la suma de los demás elementos del vector")
