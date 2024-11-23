print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def es_palindromo(palabra):
    """
    esta funcion recibe una palabra y devuelve True si es un palindromo, 
    de lo contrario devuelve False.

    parametros:
    palabra (str): la palabra a comprobar.

    retorna:
    bool: True si la palabra es un palindromo, False si no lo es.
    """
    # convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = palabra.lower()
    
    # comprobar si la palabra es igual a su inversión
    return palabra == palabra[::-1]

print(es_palindromo("radar"))  # salida
print(es_palindromo("hola"))   # salida
print(es_palindromo("Anilina"))  # salida
print(es_palindromo("civic"))  # salida
