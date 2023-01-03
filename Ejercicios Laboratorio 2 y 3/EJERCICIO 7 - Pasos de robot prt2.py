#TOMAMOS LA MISMA IDEA DEL EJERCICIO ANTERIOR PERO ESTA VEZ CAUNDO ESTE ROBOT DE UN PASO MAS:
def pasos_robot(n):
    if n==1 or n==2:
        return n
    elif n==3:
        return n+1
    return pasos_robot(n-1) + pasos_robot(n-2) + pasos_robot(n-3)

