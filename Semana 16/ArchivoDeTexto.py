# --------------------------------------------
# Trabajo con Archivos de Texto en Python
# Autor: Leonardo Córdova
# Descripción: Escritura, lectura y cierre de archivos .txt
# --------------------------------------------

# 1. Escritura de Archivo de Texto
# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
# Si el archivo no existe, Python lo crea automáticamente
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write()
archivo.write("1. Hoy aprendí a trabajar con archivos en Python.\n")
archivo.write("2. El método w rite () se utiliza para escribir texto en el archivo.\n")
archivo.write("3. Siempre debo cerrar el archivo después de usarlo para liberar recursos.\n")

# Cerramos el archivo después de escribir
archivo.close()
print("Archivo 'my_notes.txt' creado y guardado correctamente.\n")

# 2. Lectura de Archivo de Texto
# Abrimos el archivo nuevamente, esta vez en modo lectura ('r')
archivo = open("my_notes.txt", "r")

print(" Leyendo el contenido del archivo línea por línea:\n")

# Leemos cada línea del archivo con readline() dentro de un bucle
linea = archivo.readline()
while linea:
    print(linea.strip())  # strip() elimina los saltos de línea al final
    linea = archivo.readline()

# 3. Cierre de Archivos
archivo.close()
print("\n Archivo cerrado correctamente.")
