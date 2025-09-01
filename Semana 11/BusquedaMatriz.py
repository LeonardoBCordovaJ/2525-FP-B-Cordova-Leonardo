# Programa 1: Búsqueda en una matriz bidimensional

def buscar_valor(matriz, valor):
    """
    Busca un valor en la matriz y devuelve su posición si existe.
    """
    for i in range(len(matriz)):           # Recorre filas
        for j in range(len(matriz[i])):    # Recorre columnas
            if matriz[i][j] == valor:
                return i, j   # Retorna posición (fila, columna)
    return None


# Definimos una matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor a buscar
valor_buscado = 0

# Llamamos a la función
posicion = buscar_valor(matriz, valor_buscado)

# Mostramos resultados
if posicion:
    print(f"✅ El valor {valor_buscado} se encontró en la posición (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"❌ El valor {valor_buscado} NO se encontró en la matriz.")
