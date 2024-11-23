print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def procedimiento(lista):
    """
    esta funcion recibe una lista de numeros enteros y imprime un histograma
    en la pantalla, donde cada número se representa por una serie de asteriscos.

    parametros:
    lista (list): una lista de números enteros para generar el histograma.
    """
    # recorrer cada número de la lista
    for numero in lista:
        # imprimir una cantidad de asteriscos igual al valor del número
        print('*' * numero)

procedimiento([4, 9, 7])
