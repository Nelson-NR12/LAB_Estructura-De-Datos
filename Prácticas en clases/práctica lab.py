class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listadoble:
    def _init_(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregar_final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
            self.size +=1
    
    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
            self.size +=1
    def recorrer_inicio_final(self):
        aux = self.primero
        while aux!= None:
            print(aux.dato)
            aux = aux.siguiente

    def recorrer_fin_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior  

    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None 
            self.size -=1

    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size =0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size-=1

            #MENU DE OPCIONES
try:
    if __name__ == "__main__":
        opcion = 0
        lista = listadoble()

        while opcion !=8:
            print("Lista doble: \n 1.lista vacia?: \n 2. Agregar final\n 3. agregar inicio\n 4. Recorrer inicio - final\n 5. Recorrer final - inicio\n 6. Eliminar inicio\n 7. Eliminar final \n 8. Salir")
            opcion = int(input("Ingrese opcion"))

            if opcion == 1:
                print("Si"if lista.vacia()else "No")
            elif opcion == 2:
                dato = input("Ingrese un dato")
                lista.agregar_final(dato)
            elif opcion == 3:
                dato = input("Ingrese un dato")
                lista.agregar_inicio(dato)
            elif opcion == 4:
                lista.recorrer_inicio_final()
            elif opcion == 5:
                lista.recorrer_fin_inicio()
            elif opcion == 6:
                lista.eliminar_inicio()
            elif opcion == 7:
                lista.eliminar_final()
            elif opcion == 8:
                print("FIN")
            else:
                print("Ingrese dato correcto: ")

except Exception as e:
    print(e)