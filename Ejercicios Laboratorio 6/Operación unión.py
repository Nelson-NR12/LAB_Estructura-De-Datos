frutas_1 = {"manzana", "plátano", "pera"}
frutas_2 = {"fresa", "plátano", "kiwi"}
frutas_3 = {"naranja", "plátano", "mango"}

# Unión con operadores
frutas_union = frutas_1 | frutas_2 | frutas_3
print(frutas_union)

# Unión con el método union()
frutas_union = frutas_1.union(frutas_2, frutas_3)
print(frutas_union) 

