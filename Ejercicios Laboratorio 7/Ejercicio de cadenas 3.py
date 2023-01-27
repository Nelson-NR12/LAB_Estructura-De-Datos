def dividir_cadena(string, separator):
    # Utilizar el método split() de las cadenas
    substrings = string.split(separator)
    return substrings

# Ejemplo de uso
print(dividir_cadena("esto-es-una-prueba", "-")) 
print(dividir_cadena("1,2,3,4,5", ",")) 
