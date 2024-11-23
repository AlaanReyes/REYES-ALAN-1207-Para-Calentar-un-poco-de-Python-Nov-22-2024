print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def inversa(cadena):
    """
    esta funcion recibe una cadena de texto y devuelve la inversion de esa cadena.

    parametros:
    cadena (str): la cadena de texto a invertir.

    retorna:
    str: la cadena invertida.
    """
    # invertir la cadena utilizando slicing
    return cadena[::-1]
print(inversa("estoy probando"))  # salida
print(inversa("hola"))  # salida
print(inversa("12345"))  # salida
