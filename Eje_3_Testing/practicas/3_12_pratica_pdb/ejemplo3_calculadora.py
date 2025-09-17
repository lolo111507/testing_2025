# Script calculadora con error en funciones
def sumar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def calculadora(x, y):
    s = sumar(x, y)
    m = multiplicar(x, y)
    return s, m

print(calculadora(5, 3))
