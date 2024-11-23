print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def es_vocal(caracter):
    """
    esta funcion recibe un caracter y devuelve True si es una vocal, 
    de lo contrario devuelve False.

    parametros:
    caracter (str): el caracter a comprobar.

    retorna:
    bool: True si el caracter es una vocal, False si no lo es.
    """
    # comprobar si el caracter es una vocal
    if caracter.lower() in 'aeiou':
        return True
    return False

print(es_vocal('a'))  # salida
print(es_vocal('A'))  # salida
print(es_vocal('b'))  # salida
print(es_vocal('E'))  # salida
print(es_vocal('z'))  # salida
