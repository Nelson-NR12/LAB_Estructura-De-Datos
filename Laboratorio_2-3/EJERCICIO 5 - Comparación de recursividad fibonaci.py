import time
def fibonaci_Rec(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return fibonaci_Rec(numero-1)+ fibonaci_Rec(numero-2)
tempoA=time.perf_counter()
fibonaci_Rec(10)
tempoB=time.perf_counter()
print ("TIEMPO DE RESPUESTA RECURSIVO:" ,tempoB-tempoA)

def fibonaci(n):
    a = 0
    b = 1
    for k in range(n+1):
        с = b+a
        a = b
        b = с
    return a
tempo1=time.perf_counter()
fibonaci(10)
tempo2=time.perf_counter()
print( "TIEMPO DE RESPUESTA NO RECURSIVO:",tempo2-tempo1)