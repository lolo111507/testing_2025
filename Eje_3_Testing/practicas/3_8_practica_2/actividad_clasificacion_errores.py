# Script de práctica – Clase 2
# Menú interactivo para probar distintos errores

def error_sintaxis():
    # ❌ Ejemplo: error de sintaxis
    # La siguiente línea está comentada porque impediría ejecutar el script.
    def saludo(nombre)   # falta :
    print("Este ejemplo se explica en la chuleta (no se puede ejecutar con el error real).")

def error_variable_indefinida():
    print("Accediendo a una variable inexistente...")
    print(resultado)   # ❌ 'resultado' no está definido

def error_logico_suma():
    def sumar(a, b):
        return a - b   # ❌ lógica incorrecta
    print("Probando suma 5 + 3:", sumar(5, 3))

def error_division_cero():
    print("División entre cero...")
    x = 10 / 0   # ❌ ZeroDivisionError
    print(x)

def error_bucle_infinito():
    print("Atención: esto generaría un bucle infinito. Se corta con Ctrl+C")
    contador = 0
    while contador < 5:
        print("Contando:", contador)
        # ❌ falta contador += 1 → bucle infinito

def error_tipo_dato():
    print("Sumando número y texto...")
    numero = 5 + "2"   # ❌ TypeError
    print(numero)

def menu():
    while True:
        print("\n=== Menú de errores ===")
        print("1. Error de Sintaxis")
        print("2. Error de Variable indefinida")
        print("3. Error lógico (suma)")
        print("4. Error de división por cero")
        print("5. Error de bucle infinito")
        print("6. Error de tipo de dato (int + str)")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            error_sintaxis()
        elif opcion == "2":
            error_variable_indefinida()
        elif opcion == "3":
            error_logico_suma()
        elif opcion == "4":
            error_division_cero()
        elif opcion == "5":
            error_bucle_infinito()
        elif opcion == "6":
            error_tipo_dato()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
