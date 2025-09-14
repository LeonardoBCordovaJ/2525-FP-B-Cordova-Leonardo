# ==========================
# Programa: Calcular temperaturas promedio
# Autor: [Leonardo Benjamin Córdova Jaramillo]
# Descripción:
#   Este programa calcula el promedio de temperaturas
#   de varias ciudades usando funciones en Python.
# ==========================

# Lista de ciudades
ciudades = ["Huaquillas", "Loja", "El Coca"]

# Datos de temperaturas (3D: ciudades -> semanas -> días)
temperaturas = [
    [   # Ciudad 1 - Huaquillas
        [ {"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 29},
          {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 33}, {"day": "Domingo", "temp": 30} ],
        [ {"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 31},
          {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 29} ],
        [ {"day": "Lunes", "temp": 28}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 32},
          {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 33}, {"day": "Domingo", "temp": 30} ],
        [ {"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 29}, {"day": "Miércoles", "temp": 31},
          {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 29} ]
    ],
    [   # Ciudad 2 - Loja
        [ {"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 19},
          {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 23}, {"day": "Domingo", "temp": 20} ],
        [ {"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21},
          {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 19} ],
        [ {"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20},
          {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 19} ],
        [ {"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21},
          {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 23}, {"day": "Domingo", "temp": 21} ]
    ],
    [   # Ciudad 3 - El Coca
        [ {"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 14},
          {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 15} ],
        [ {"day": "Lunes", "temp": 14}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 16},
          {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 13}, {"day": "Domingo", "temp": 14} ],
        [ {"day": "Lunes", "temp": 13}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 17},
          {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 14}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 15} ],
        [ {"day": "Lunes", "temp": 14}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 15},
          {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 14} ]
    ]
]

# ==========================
# Función para calcular el promedio de temperatura
# ==========================
def calcular_promedios(datos, nombres_ciudades):
    """
    Calcula y muestra el promedio de temperaturas por semana para cada ciudad.
    :param datos: lista 3D de temperaturas (ciudad -> semana -> días)
    :param nombres_ciudades: lista con nombres de ciudades
    """
    for ciudad_idx, ciudad in enumerate(datos):  # Iterar por ciudad
        print(f"\nPromedios de temperaturas en {nombres_ciudades[ciudad_idx]}:")
        for semana_idx, semana in enumerate(ciudad):  # Iterar por semana
            suma = sum([dia["temp"] for dia in semana])
            promedio = suma / len(semana)
            print(f"  Semana {semana_idx + 1}: {promedio:.2f} °C")

# ==========================
# Ejecución del programa
# ==========================
calcular_promedios(temperaturas, ciudades)