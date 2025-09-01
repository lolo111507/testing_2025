def dividir(a, b):
    a = int(a)  # Corregido para convertir a int
    b = int(b)  # Corregido para convertir a int
    
    if b == 0:
        return "Error: División por cero"
    elif b is None:
        return "Error: Falta el segundo operando"
    else:
        return a / b


print("Resultado:", dividir(10, 2)) #sintaxis
print("Resultado:", dividir(15, "3"))
print("Resultado:", dividir(10, 0))
print("Resultado:", dividir(10, None)) #tipo de dato
print("Resultado:", dividir(10, "a")) #tipo de dato
print("Resultado:", dividir("10", 2)) #tipo de dato
print("Resultado:", dividir("diez", 2)) #tipo de dato
print("Resultado:", dividir(10)) #variable indefinida
print("Resultado:", dividir(10, 2, 5)) #variable indefinida
print("Resultado:", dividir(10, 2, 5, 1)) #variable indefinida
print("Resultado:", dividir()) #variable indefinida
print("Resultado:", dividir(10, 2, 5, 1, 0))