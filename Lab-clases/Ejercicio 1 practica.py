# Importamos el módulo array
import array
# Pedimos al usuario que ingrese el tamaño de los arrays
size = int(input("Ingresa el tamaño de los arrays: "))

# Creamos el array para almacenar los nombres
names = array.array('u', ['0'] * size)

# Creamos el array para almacenar la longitud de los nombres
lengths = array.array('i1', [0] * size)

# Pedimos al usuario que ingrese los nombres de las personas
for i in range(size):
    names[i] = input("Ingresa el nombre de la persona {}: ".format(i+1))
    lengths[i] = len(names[i])

# Imprimimos los arrays
print("Nombres:", names)
print("Longitudes:", lengths)
