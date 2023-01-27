def es_polidromo(string):
    # Invertir la cadena
    reversed_string = string[::-1]
    # Comparar la cadena original con la invertida
    if string == reversed_string:
        return True
    else:
        return False

# Ejemplo de uso
print(es_polidromo("abba")) 
print(es_polidromo("abc")) 
