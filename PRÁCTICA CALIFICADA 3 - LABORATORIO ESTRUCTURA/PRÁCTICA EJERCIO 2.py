# DEFINIMOS LA LITSA DE TAREAS
tareas_pendientes = []

# REALIZAMOS UNA FUNCION PARA GREGAR UNA TAREA AL INICIO 
def agregar_tarea():
    tarea = input("Ingrese la tarea que desea agregar: ")
    tareas_pendientes.insert(0, tarea)
    print(f"Se agregó '{tarea}' al inicio de la lista.")

# HACEMOS OTRA FUNCION PARA ELIMIANR UNA TAREA AL FINAL DE LA LISTA
def eliminar_tarea():
    if tareas_pendientes:
        tarea_eliminada = tareas_pendientes.pop()
        print(f"Se eliminó '{tarea_eliminada}' del final de la lista.")
    else:
        print("La lista de tareas está vacía.")
# Función para mostrar todas las tareas en orden inverso al que se agregaron
def mostrar_tareas():
    if tareas_pendientes:
        print("Tareas pendientes (en orden inverso al que se agregaron):")
        for i, tarea in enumerate(reversed(tareas_pendientes), start=1):
            print(f"{i}. {tarea}")
    else:
        print("La lista de tareas está vacía.")

# REALIZAMMOS UNA FUNCION DE TAL MODO QUE CUENTE LA CANTIDAD TOTAL DE TAREAS DENTRO MDE LA LISTA
    cantidad_tareas = len(tareas_pendientes)
    if cantidad_tareas == 1:
        print("Hay 1 tarea pendiente en la lista.")
    else:
        print(f"Hay {cantidad_tareas} tareas pendientes en la lista.")

# Función para contar la cantidad total de tareas en la lista
def contar_tareas():
    cantidad_tareas = len(tareas_pendientes)
    if cantidad_tareas == 1:
        print("Hay 1 tarea pendiente en la lista.")
    else:
        print(f"Hay {cantidad_tareas} tareas pendientes en la lista.")

#FINALMENTE PARA INTERACTUAC CON EL PROGRMA AGREAGAMOS UN MENU 
while True:
    print("\n***HISTORIAL DE TAREAS PENDIENTES***")
    print("1. AGREGAR UNA TAREA LA INICIO DE LA LISTA")
    print("2. ELIMAR UNA TAREA AL FINAL DE LA LISTA")
    print("3. MOSTRAR LA LISTA DE TAREAS EN ORDEN INVERSO")
    print("4. CONTAR LA CANTIDAD DE TAREAS TOTALES EN LA LISTA")
    print("5. SALIR")
    opcion = input("SELECCIONE UNA OPCION: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        mostrar_tareas()
    elif opcion == "4":
        contar_tareas()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")

   