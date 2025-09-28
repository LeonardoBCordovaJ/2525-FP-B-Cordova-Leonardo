# ============================
# Diccionario de Información Personal
# ============================

# 1) Crear diccionario con valores fijos
informacion_personal = {
    "Nombre": "Benjamin Jaramillo",
    "Edad": 31,
    "Ciudad": "Guayaquil"
}
# 1) Imprimir el Diccionario Inicial
print("____________________")
print("Diccionario Inicial:")
print("____________________")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# 2) Modificar ciudad
informacion_personal["Ciudad"] = "Cuenca"

# 3) Agregar/Actualizar profesión
informacion_personal["Profesion"] = "Ingeniero en Tecnologías de La Información"

# 4) Verificar clave "telefono"
if "Teléfono" not in informacion_personal:
    informacion_personal["Teléfono"] = "+593-999-111-222"

# 5) Eliminar edad
informacion_personal.pop("Edad") #Elimina la Edad

# 6) Imprimir resultado
print()
print("___________________")
print("Diccionario Final:")
print("___________________")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")