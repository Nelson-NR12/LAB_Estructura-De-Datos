def frecuencia_de_caracter(string):
    # Inicializar el diccionario vacío
    frequency = {}
    # Iterar sobre cada caracter de la cadena
    for char in string:
        # Si el caracter ya está en el diccionario, aumentar su contador
        if char in frequency:
            frequency[char] += 1
        # Si el caracter no está en el diccionario, agregarlo con contador 1
        else:
            frequency[char] = 1
    return frequency

# Ejemplo de uso
print(frecuencia_de_caracter("Hola mundo")) 
print(frecuencia_de_caracter("mi casa")) 
