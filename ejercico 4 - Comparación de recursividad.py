#Primero elaboramos un algoritmo no recursivo de la siguiente manera:
import time
def factorial(n):
    b=1
    for i in range(n,1,-1):
        b=b*i
    return b
tempoA=time.perf_counter()
fact=factorial(7)
tempoB=time.perf_counter()
print("EL FACTORIAL ES: ",fact,"\nTIEMPO DE EJECUCION: ",tempoB-tempoA)

#EN ESTA SEGUNDA PARTE REALIZAREMOS EL FACTORIAL PERO USANDO LA RECURSIVIDAD COMO UNA METODOLOGÍA.

def factorial_Rec(n):
    if n == 1:
         return 1
    return n*factorial_Rec(n-1)
tempo1=time.perf_counter()
fact1=factorial_Rec(7)
tempo2=time.perf_counter()
print("EL FACTORIAL ES: ",fact1,"\nTIEMPO DE EJECUCION: ",tempo2-tempo1)