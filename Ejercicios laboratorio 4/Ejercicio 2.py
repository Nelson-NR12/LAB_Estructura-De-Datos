tamaño = int(input("Ingrese el tamaño del array: "))
array = list(range(1,tamaño+1))

def fill_array(array, numero):
  for i in range(len(array)):
    array[i] = (i+1)* numero

numero = int(input("Ingrese un número: "))
fill_array(array, numero)

print(array)  # Mostramos en pantalla el array rellenado
