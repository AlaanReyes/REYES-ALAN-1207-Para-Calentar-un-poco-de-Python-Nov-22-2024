print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def sum_lista(lista):
    """
    esta funcion toma una lista de numeros y devuelve la suma de todos ellos.

    parametros:
    lista (list): una lista de numeros a sumar.

    retorna:
    int o float: la suma de todos los numeros de la lista.
    """
    total = 0
    for num in lista:
        total += num
    return total

def multip_lista(lista):
    """
    esta funcion toma una lista de numeros y devuelve el producto de todos ellos.

    parametros:
    lista (list): una lista de numeros a multiplicar.

    retorna:
    int o float: el producto de todos los numeros de la lista.
    """
    total = 1
    for num in lista:
        total *= num
    return total

# Sumar los números de una lista
print(sum_lista([1, 2, 3, 4]))  # salida

# Multiplicar los números de una lista
print(multip_lista([1, 2, 3, 4]))  # salida

