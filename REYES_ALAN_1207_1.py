print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def max_personalizado(a, b):
    """
    esta funcion recibe dos numeros y devuelve el mayor de los dos.

    parametros:
    a (int o float): primer numero a comparar.
    b (int o float): segundo numero a comparar.

    retorna:
    el numero mayor entre a y b.
    """
    # comparar los dos numeros y devolver el mayor
    if a > b:
        return a
    return b

print(max_personalizado(7, 6))  # salida
print(max_personalizado(3.8, 25.9))  # salida
