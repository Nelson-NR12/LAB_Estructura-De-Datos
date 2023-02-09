def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j] :
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = clave

lista = [9, 1, 8, 2, 7, 3, 6, 4, 5]
ordenamiento_insercion(lista)
print("Lista ordenada:", lista)
