import random #IMPORTAMOS UNA LIBRERIA PARA ESTE EJERCICIO 
def desordenar(lista,list_larg,contador):
    if contador < list_larg:
        Numero_radom = random.randint(contador,list_larg - 1)
        lista [contador],lista[Numero_radom] = lista[Numero_radom],lista[contador]
        desordenar(lista,list_larg,contador + 1)
lista_de_numeros=[5,10,15,20,25,30,35,40]
desordenar(lista_de_numeros,len(lista_de_numeros),0)
print(lista_de_numeros)