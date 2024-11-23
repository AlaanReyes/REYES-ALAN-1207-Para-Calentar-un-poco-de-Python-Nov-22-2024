print(" ") #espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #info programador
print(" ") #espacio

def max_de_tres(a, b, c):
    """
    esta funcion recibe tres numeros y devuelve el mayor de los tres.

    parametros:
    a (int o float): primer numero a comparar.
    b (int o float): segundo numero a comparar.
    c (int o float): tercer numero a comparar.

    retorna:
    el numero mayor entre a, b y c.
    """
    # encontrar el mayor de los tres numeros
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

print(max_de_tres(3, 5, 2))  # salida
print(max_de_tres(7, 6, 7))  # salida
print(max_de_tres(1.5, 2.5, 1.0))  # salida
