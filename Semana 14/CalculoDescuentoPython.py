# Autor: Leonardo Córdova
# Programa: Calcular descuento en compras (versión con entrada de datos)
# Descripción:
#   Este programa permite al usuario ingresar el monto de la compra en dólares
#   y el porcentaje de descuento que desea aplicar. Si el usuario no indica
#   porcentaje, se aplicará automáticamente un 10% por defecto.
#   Se muestran el valor del descuento y el monto final a pagar.

# ---------------------------------------------------------------
# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a partir del monto total de la compra.

    Parámetros:
        monto_total (float): El valor total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento (por defecto 10%).

    Retorna:
        float: El valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# ---------------------------------------------------------------
# Programa principal
if __name__ == "__main__":
    print("=== CÁLCULO DE DESCUENTO EN COMPRAS ===")

    # 1. Primera compra con descuento predeterminado (10%)
    monto1 = float(input("Ingrese el monto de la compra 1 en dólares: $"))
    descuento1 = calcular_descuento(monto1)  # usa el 10% por defecto
    monto_final1 = monto1 - descuento1

    print("\nCompra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")
    print("-" * 40)

    # 2. Segunda compra con porcentaje de descuento elegido por el usuario
    monto2 = float(input("Ingrese el monto de la compra 2 en dólares: $"))
    porcentaje2 = float(input("Ingrese el porcentaje de descuento a aplicar: "))
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print("\nCompra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2:.0f}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")