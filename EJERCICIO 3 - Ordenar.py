#mantenemos la misma idea del algoritmo usado anteriormente
def select_orden(lista, list_large, contador):
         if contador<list_large:
                 pequeño  = lista[contador]
                 posicion = contador
                 for i in range(contador+1, list_large):
                          if lista[i]<pequeño:
                                  pequeño  = lista[i]
                                  posicion = i
                 lista[contador],lista [posicion]=lista[posicion], lista[contador]
                 select_orden(lista, list_large, contador+1)
Lista_de_numeros=[25,96,12,45,63,87,18,9,5,1]
select_orden(Lista_de_numeros,len(Lista_de_numeros),0)
print(Lista_de_numeros)