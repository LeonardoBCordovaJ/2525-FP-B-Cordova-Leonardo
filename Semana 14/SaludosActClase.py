#Definir funciones

def saludar(nombre):
    mensaje_saludo = f'Hola {nombre}. Bienvenido a nuestro congreso'
    return mensaje_saludo

#Llamado a la funcion
nombre = input('Ingresa tu nombre: ')
print(saludar(nombre))
