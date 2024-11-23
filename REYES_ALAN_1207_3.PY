print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def calcular_longitud(entrada):
    """
    esta funcion recibe una lista o una cadena y devuelve su longitud.

    parametros:
    entrada (lista o cadena): el objeto cuya longitud se quiere calcular.

    retorna:
    int: la longitud de la lista o la cadena.
    """
    # iniciar un contador en 0
    contador = 0
    
    # recorrer cada elemento de la entrada
    for elemento in entrada:
        contador += 1
    
    return contador

# Usando una lista
mi_lista = [1, 2, 3, 4]
print(calcular_longitud(mi_lista))  # salida

# Usando una cadena
mi_cadena = "hola"
print(calcular_longitud(mi_cadena))  # salida
