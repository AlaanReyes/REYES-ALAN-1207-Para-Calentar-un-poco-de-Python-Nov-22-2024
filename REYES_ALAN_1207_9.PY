print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def generar_n_caracteres(n, caracter):
    """
    esta funcion recibe un entero n y un caracter, y devuelve una cadena 
    que contiene el caracter repetido n veces.

    parametros:
    n (int): el numero de veces que se debe repetir el caracter.
    caracter (str): el caracter que se va a repetir.

    retorna:
    str: una cadena con el caracter repetido n veces.
    """
    # devolver el caracter repetido n veces
    return caracter * n

print(generar_n_caracteres(5, "x"))  # salida
print(generar_n_caracteres(3, "*"))  # salida
print(generar_n_caracteres(7, "a"))  # salida
print(generar_n_caracteres(0, "z"))  # salida
