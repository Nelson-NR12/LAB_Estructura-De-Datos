notas = [20, 15, 12, 11, 8, 4, 1]

# Buscamos la nota mínima
min_nota = float('inf')  # Inicializamos la nota mínima con un valor muy alto
for nota in notas:
  if nota < min_nota:
    min_nota = nota

# Eliminamos la nota mínima de la lista
notas.remove(min_nota)

# Mostramos en pantalla la nota mínima eliminada
print(f"La nota mínima eliminada fue {min_nota}")

# Calculamos el promedio de las notas
total = sum(notas)
promedio = total / len(notas)

# Mostramos en pantalla el promedio
print(f"El promedio de las notas es {promedio:.2f}")
