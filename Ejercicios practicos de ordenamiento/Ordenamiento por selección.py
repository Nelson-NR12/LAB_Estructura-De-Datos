def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

lista = [9, 1, 8, 2, 7, 3, 6, 4, 5]
ordenamiento_seleccion(lista)
print("Lista ordenada:", lista)
