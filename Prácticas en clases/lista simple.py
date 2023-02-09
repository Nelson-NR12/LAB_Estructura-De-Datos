class Nodo:

    def __init__(self,dato):
        self.dato = dato
        self.next = None
class ListaSimpleEnlasada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.next = Nodo(dato)

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.next

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.next != self.ultimo:
            aux = aux.next
        aux.next = None
        self.ultimo = aux

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo()
        else:
            aux = Nodo(dato)
            aux.next = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        self.primero = self.primero.next

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaSimpleEnlasada()

        while opcion !=7:
            print("Lista simple enlazada: \n 1.agregar ultimo\n 2. Eliminar ultimo\n 3.Lista vacia?\n 4. Agregar inicio\n 5. Eliminar inicio\n 6. Mostrar toda la lista\n 7.salir")
            opcion = int(input("Ingrese opcion"))

            if opcion == 1:
                dato = input("Ingrese un dato")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("Si"if lista.vacia()else "No")
            elif opcion == 4:
                dato = input("Ingrese un dato")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrido()
            elif opcion == 7:
                print("FIN")
            else:
                print("Ingrese dato correcto: ")

except Exception as e:
    print(e)