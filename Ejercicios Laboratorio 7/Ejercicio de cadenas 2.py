def Longitud_subcadena(string):
    # Inicializar variables
    max_length = 0
    current_length = 0
    substring = ""
    substring_set = set()
    # Iterar sobre cada caracter de la cadena
    for char in string:
        # Si el caracter no está en el conjunto, agregarlo y aumentar la longitud actual
        if char not in substring_set:
            substring_set.add(char)
            current_length += 1
        # Si el caracter ya está en el conjunto, actualizar la longitud máxima si es necesario
        # y vaciar el conjunto
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
            substring_set.clear()
    # Retornar la longitud máxima
    return max_length

# Ejemplo de uso
print(Longitud_subcadena("abcabcbb")) # 3 (la subcadena "abc")
print(Longitud_subcadena("bbbbb")) # 1 (la subcadena "b")
