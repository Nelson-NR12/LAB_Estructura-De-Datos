class pila:
    def _init_(self,size):
        self.lista = []
        self.tope = 0
        self.size = size
    
    def empty(self):
        if self.tope==0:
            return True
        else:
            return False
    def push(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            self.size +=5
            self.lista = [dato]
            self.tope +=1

    def pop(self):
        if self.empty():
            print("La pila est+a vacía")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range (self.tope)]

    def show(self):
        i = self.tope
        while i > -1:
            print(f"[{i}] >> {self.lista[i]}")
            i -=1

    def lifoShow(self):
        return self.lista[-1]
    
try:
    if __name__ == "__main__":
        opcion = 0
        lista = pila()

        while opcion !=6:
            print("pilas: \n 1.empty: \n 2. push\n 3. agregar inicio\n 4. pop\n 5. show\n 6. Salir")
            opcion = int(input("Ingrese opcion"))

            if opcion == 1:
                print("Si"if pila.empty()else "No")
            elif opcion == 2:
                dato = input("Ingrese un dato")
                pila.push(dato)
            elif opcion == 3:
                dato = input("Ingrese un dato")
                pila.pop(dato)
            elif opcion == 4:
                dato = input("Ingrese un dato")
                pila.show(dato)
            elif opcion == 5:
                dato = input("Ingrese un dato")
                pila.lifoShow(dato)
            elif opcion == 6:
                print("FIN")
            else:
                print("Ingrese dato correcto: ")

except Exception as e:
    print(e)