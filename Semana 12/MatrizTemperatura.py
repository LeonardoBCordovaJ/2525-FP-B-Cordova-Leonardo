# ==========================
# Programa: Promedio de temperaturas
# ==========================

# Lista de ciudades
ciudades = ["Huaquillas", "Loja", "El Coca"]

# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días con nombre y temperatura)
temperaturas = [
    [   # Ciudad 1 - Guayaquil
        [ # Semana 1
            {"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 33}, {"day": "Domingo", "temp": 30}
        ],
        [ # Semana 2
            {"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 29}
        ],
        [ # Semana 3
            {"day": "Lunes", "temp": 28}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 33}, {"day": "Domingo", "temp": 30}
        ],
        [ # Semana 4
            {"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 29}, {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Ciudad 2 - Quito
        [ # Semana 1
            {"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 23}, {"day": "Domingo", "temp": 20}
        ],
        [ # Semana 2
            {"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 19}
        ],
        [ # Semana 3
            {"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 19}
        ],
        [ # Semana 4
            {"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 23}, {"day": "Domingo", "temp": 21}
        ]
    ],
    [   # Ciudad 3 - Cuenca
        [ # Semana 1
            {"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 15}
        ],
        [ # Semana 2
            {"day": "Lunes", "temp": 14}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 13}, {"day": "Domingo", "temp": 14}
        ],
        [ # Semana 3
            {"day": "Lunes", "temp": 13}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 14}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 15}
        ],
        [ # Semana 4
            {"day": "Lunes", "temp": 14}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 14}
        ]
    ]
]

# ==========================
# Calcular promedio de temperaturas
# ==========================
for ciudad_idx, ciudad in enumerate(temperaturas):  # Itera por ciudad
    print(f"\nPromedios de temperaturas en {ciudades[ciudad_idx]}:")
    for semana_idx, semana in enumerate(ciudad):   # Itera por semana
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"  Semana {semana_idx + 1}: {promedio:.2f} °C")
