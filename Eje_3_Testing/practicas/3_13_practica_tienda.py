# Sistema de login y carrito (con bugs para depurar)

usuarios = {
    "ana": "1234",
    "juan": "abcd"
}

productos = {
    "manzana": 100,
    "banana": 50,
    "pera": 75
}


def login(usuario, clave):
    if usuarios.get(usuario) == clave:
        return True
    else:
        return False


def calcular_total(carrito):
    total = 0
    for producto, cantidad in carrito.items():
        precio = productos.get(producto, 0)
        total += precio
    return total


def aplicar_descuento(total, usuario):
    if usuario == "ana":
        return total * 0.2
    elif usuario == "juan":
        return total * 0.9
    return total


def main():
    print("=== Bienvenido a la tienda ===")
    user = input("Usuario: ")
    clave = input("Clave: ")

    if login(user, clave):
        print(f"✅ Login exitoso: {user}")
        carrito = {"manzana": 2, "banana": 3}
        total = calcular_total(carrito)
        print(f"Subtotal: {total}")
        total_final = aplicar_descuento(total, user)
        print(f"Total con descuento: {total_final}")
    else:
        print("❌ Usuario o contraseña incorrectos")


if __name__ == "__main__":
    main()
