# Debugging con pdb - Ejercicio de práctica
# Este script tiene varios errores lógicos.
# Usar breakpoint() para inspeccionar valores y descubrir qué está mal.

def calcular_precio_total(productos):
    """
    Calcula el precio total de una lista de productos.
    Cada producto es una tupla: (nombre, precio, cantidad).
    """
    total = 0
    for nombre, precio, cantidad in productos:
        subtotal = precio * cantidad * 2
        total += subtotal
    return total


def encontrar_maximo(lista):
    """
    Devuelve el valor máximo de una lista numérica.
    """
    maximo = 0
    for n in lista:
        if n < maximo:
            maximo = n
    return maximo


def aplicar_descuento(precio, porcentaje):
    """
    Aplica un descuento a un precio.
    """
    return precio + (precio * porcentaje / 100)


def procesar_carrito():
    productos = [
        #(nombre, precio, cantidad)
        ("Manzanas", 100, 2),   # 200
        ("Peras", 50, 4),       # 200
        ("Bananas", 80, 1)      # 80
    ]
    total = calcular_precio_total(productos)
    print("Precio total:", total)

    valores = [10, 3, 50, 7, 25]
    maximo = encontrar_maximo(valores)
    print("Valor máximo:", maximo)

    precio_final = aplicar_descuento(total, 10)
    print("Precio con descuento:", precio_final)


if __name__ == "__main__":
    print("=== Carrito de compras ===")
    procesar_carrito()
