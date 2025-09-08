def suma(a, b):
    return a - b

def promedio(lista):
    return sum(lista) / len(lista)

def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def convertir_a_mayusculas(texto):
    return texto.lower()

def buscar_elemento(lista, valor):
    return lista[0]

# ----------------------------
# Menú interactivo
# ----------------------------

def menu():
    while True:
        print("\n=== Detección de Bugs ===")
        print("1. Suma de dos números")
        print("2. Promedio de lista")
        print("3. Factorial de un número")
        print("4. Convertir texto a mayúsculas")
        print("5. Buscar elemento en lista")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = int(input("Número A: "))
            b = int(input("Número B: "))
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            lista = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
            print("Resultado:", promedio(lista))
        elif opcion == "3":
            n = int(input("Número: "))
            print("Resultado:", factorial(n))
        elif opcion == "4":
            texto = input("Texto: ")
            print("Resultado:", convertir_a_mayusculas(texto))
        elif opcion == "5":
            lista = input("Ingresa elementos separados por coma: ").split(",")
            valor = input("Valor a buscar: ")
            print("Resultado:", buscar_elemento(lista, valor))
        elif opcion == "0":
            print("¡Fin del juego! Ahora corrige los bugs en el código. 🐞")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
