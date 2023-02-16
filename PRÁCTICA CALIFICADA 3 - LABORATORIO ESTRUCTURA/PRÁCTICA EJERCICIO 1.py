# PRIMERO DEFINIMOS LA LISTA DE COMPRAS
lista_de_compras = []

# FUNCION PARA AGREGAR UN PRODUCTO AL FINAL
def agregar_producto():
    producto = input("INGRESA UN PODUCTO PARA AGREGAR: ")
    lista_de_compras.append(producto)
    print(f"SE AGERGÓ '{producto}' A LA LISTA DE COMPRAS")

# FUNCION PARA ELIMIANR EL PRIMERO DE LA LISTA DE PRODUCTOS
def eliminar_producto():
    if lista_de_compras:
        producto_eliminado = lista_de_compras.pop(0)
        print(f"SE ELIMNO '{producto_eliminado}' DE LA LISTA DE COMPRAS")
    else:
        print("LISTA DE COMPRAS VACIA")

# MUESTRA TODOS LOS PRODUCTOS EN UNA LISTA ORDENADA
def mostrar_lista():
    if lista_de_compras:
        print("LISTA DE COMPRAS: ")
        for i, producto in enumerate(lista_de_compras, start=1):
            print(f"{i}. {producto}")
    else:
        print("LISTA DE COMPRAS VACIA")

# CREAMOS UN MENU PARA LAS FUNCIONES Y INTERACTUAR
while True:
    print("\n***LISTA DE COMPRAS***")
    print("1. AGREGAR UN PRODUCTO")
    print("2. ELIMIANR UN PRODUCTO")
    print("3. MOSTRASR LA LISTA DE PRODUCTOS")
    print("4. SALIR")
    opcion = input("SELECIONA UNA OPCION: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        mostrar_lista()
    elif opcion == "4":
        break
    else:
        print("OPCIÓN INVALIDA, VUELVA SELECIONAR UNA OPCION CORRECTA")
