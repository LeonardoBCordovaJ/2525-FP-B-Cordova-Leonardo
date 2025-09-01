# Programa 2: Ordenación de una fila específica en matriz bidimensional

def bubble_sort(fila):
    """
    Ordena una lista usando el algoritmo Bubble Sort en orden ascendente.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


# Definimos una matriz 3x3
matriz = [
    [34, 12, 25],
    [90, 11, 56],
    [78, 63, 5]
]

# Mostramos la matriz original
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (ejemplo: fila 1 → segunda fila)
indice_fila = 1

# Ordenamos esa fila usando Bubble Sort
matriz[indice_fila] = bubble_sort(matriz[indice_fila])

# Mostramos la matriz después de ordenar
print("\n📌 Matriz después de ordenar la fila", indice_fila, ":")
for fila in matriz:
    print(fila)
