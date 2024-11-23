print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def superposicion(lista1, lista2):
    """
    esta funcion recibe dos listas y devuelve True si tienen al menos un miembro en comun,
    de lo contrario devuelve False.

    parametros:
    lista1 (list): primera lista a comparar.
    lista2 (list): segunda lista a comparar.

    retorna:
    bool: True si hay al menos un elemento común, False si no lo hay.
    """
    # recorrer cada elemento de la primera lista
    for elemento1 in lista1:
        # recorrer cada elemento de la segunda lista
        for elemento2 in lista2:
            # si hay un elemento en común, devolver True
            if elemento1 == elemento2:
                return True
    # si no se encuentra ningún elemento común, devolver False
    return False

print(superposicion([1, 2, 3], [4, 5, 6]))  # salida
print(superposicion([1, 2, 3], [3, 4, 5]))  # salida
print(superposicion([7, 8, 9], [1, 7, 3]))  # salida
print(superposicion([1, 2, 3], [7, 8, 9]))  # salida
