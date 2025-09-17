# Script con error en función factorial
def factorial(n):
    breakpoint()  # Punto de depuración
    if n == 0:
        return 0
    else:
        return n * factorial(n-1)

print(factorial(5))
