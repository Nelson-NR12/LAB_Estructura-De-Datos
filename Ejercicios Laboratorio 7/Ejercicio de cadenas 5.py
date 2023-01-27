def longitud_digito_subcadena(string):
    max_length = 0
    current_length = 0
    for char in string:
        if char.isdigit():
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

# Ejemplo de uso
print(longitud_digito_subcadena("hello123world456")) 
print(longitud_digito_subcadena("h3llo123w0rld456")) 
