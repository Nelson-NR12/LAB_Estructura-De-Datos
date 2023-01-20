
# 1. creacion de conjunto:
print('1.Crear conjuntos: ')
conjunto_1 = {'juan','‘carlos','Daniel','ana', 'ana', 'jorge'}
conjunto_2 = set(['juan','carlos','Daniel','ana', 'ana', 'jorge'])
print('Contenido del conjunto uno : ', conjunto_1)
print('Cantidad de elementos del conjunto uno :', len(conjunto_1))

print('Tipo de dato de la variable Conjunto_1 es: ', type(conjunto_1))

print()

# 2. creacion de conjuntos por medio de cadenas de caracteres
print('2. creacion de conjuntos por medio de cadenas de caracteres')
frase = 'Estructura de datos curso por aprobar'

caracteres = set(frase)
print('Contenido de la variable caracteres: ', caracteres)
print( 'Cantidad! de elementos del conjunto dos :', len(caracteres))
print('Tipo de dato de la variable Conjunto_2 es: ', type(conjunto_1))

print()

# 3. creacion de un conjunto a partir de una tupla:
print('3. creacion de un conjunto a partir de una tupla:')
numeros_primos = (2,3,5,7,7,7,2,13,11,2,2,2)
print('Contenido de la variable numeros_primos: ', numeros_primos)
print( 'Cantidad de elementos de la variable numeros_primos :' , len(numeros_primos) )
print('Tipo de dato de la variable numeros_primos es: ', type(numeros_primos))

print()


primos_unicos = set(numeros_primos)

print('Contenido de la variable primos_unicos: ', primos_unicos)
print('Cantidad de elementos de la variable primos_unicos :', len(primos_unicos))
print('Tipo de dato de la variable primos_unicos es: ', type(primos_unicos))

# 4. Creacion de un conjunto (conjunto colores arcoirisl:

print('4. Creacion de un conjunto (conjunto colores arcoiris):')
c_arcoiris = {'azul', 'verde', 'rojo', 'amarillo', 'naranja', 'violeta'}
print('Contenido de la variable c_arcoiris: ', c_arcoiris)

print('Cantidad de elementos de la variable c_arcoiris :', len(c_arcoiris))
print('Tipo de dato de la variable c_arcoiris es: ', type(c_arcoiris))

print()
print('Agregar elementos al conjunto :')

c_arcoiris.add('celeste')
print('Contenido de la variable c_arcoiris: ', c_arcoiris)
print('Cantidad de elementos de la variable c_arcoiris :', len(c_arcoiris))
print('Tipo de dato de la variable c_arcoiris es: ', type(c_arcoiris))
print()

c_arcoiris.add('celeste')

#5. Iteraccion de un conjunto en un ciclo for:
print('5. Iteraccion de un conjunto en un ciclo for:')

for c in c_arcoiris:
    print(c)

# 6. Itereccion de un Conjunto en un ciclo for y qa traves de la funcion enumerate():
print('Itereccion de un Conjunto en un ciclo for y a traves de la funcion enumerate()')

for i, c in enumerate(c_arcoiris):
    print(f'Indice: {i}- color:{c}')

print()

# 7. Operador in de Pertenencia (Contencién) sobre un Objeto Conjunto
print('7. Operador in de Pertenencia (Contencién) sobre un Objeto Conjunto:')
color = 'aguamarina'
resultado = color in c_arcoiris
print('El color %s pertenece en el conjunto arcoiris?: %s' %(color, resultado))

print()

color = 'azul'
resultado = color in c_arcoiris
print('El color %s pertenece en el conjunto arcoiris?: %s' %(color, resultado))
print()

#8. Operacion de Subconjunto con el Método de Instancia issubset()
colores = {'azul', 'verde', 'amarillo'}
resultado = colores. issubset(c_arcoiris)
print('El conjunto {} es subconjunto de {}?: {}'.format(colores,c_arcoiris,resultado))
vacio={}

#9. Operaciones de Unión e Intersección entre Conjuntos con union() e intersection()

print('Operacion de Union entre Conjuntos()')
nuevos_colores = c_arcoiris.union(colores)
print()
print('Contenido de la variable nuevos_colores: ', nuevos_colores)
print('Cantidad de elementos de la variable nuevos_colores :', len(nuevos_colores))
print('Tipo de dato de la variable nuevos_coloress es: ', type(nuevos_colores) )


print('Operaciones de  Interseccion entre Conjuntos()')
interseccion = colores.intersection(c_arcoiris)
print('Contenido de la variable interseccion: ', interseccion)
print('Cantidad de elementos de la variable interseccion :', len(interseccion))
print('Tipo de dato de la variable interseccion es: ', type(interseccion))

# 10. Operacion de Superconjunto a través del Método de Instancia superset()
print('Operación de Superconjunto a través del Método de Instancia superset()')
rgb={'rojo','verde','azul'}
resultado = c_arcoiris.issuperset(rgb)
print('El conjunto {} es superconjunto de {}?: {}'.format(c_arcoiris,rgb,resultado))

#11.Diferencia de conjuntos con el operador de resta
print('Diferencia de conjuntos con el operador resta')

#A = {1,2,3}
#B = {3,4,5}
#C=A-B
diferencia = colores - c_arcoiris 
print('La diferencia entre los conjuntos colores y c_colores es: ', diferencia)
print()
diferencia = c_arcoiris - colores
print('La diferencia entre los conjuntos c_arcoiris y colores es: ', diferencia)

print()
