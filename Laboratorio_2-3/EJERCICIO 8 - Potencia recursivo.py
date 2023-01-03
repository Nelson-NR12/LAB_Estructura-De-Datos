def potencia_rec(a,b):
    if b==1:
        return a
    else:
        return potencia_rec(a,b-1)*a