animales_africa = {"león", "elefante", "rinoceronte"}
animales_asia = {"tigre", "elefante", "rinoceronte"}
animales_america = {"puma", "jaguar", "rinoceronte"}

# Diferencia simétrica entre los tres conjuntos
diferencia_simetrica = (animales_africa ^ animales_asia) ^ animales_america
print(diferencia_simetrica)  

#como en los ejemplos anteriores usaremos la librería functools

from functools import reduce
animales_africa = {"león", "elefante", "rinoceronte"}
animales_asia = {"tigre", "elefante", "rinoceronte"}
animales_america = {"puma", "jaguar", "rinoceronte"}

print(reduce(lambda a, b: a^b, [animales_africa, animales_asia, animales_america])) 

