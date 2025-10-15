def mayor(a, b):
    if a > b:
        return a
    else:
        return b

# Casos normales
assert mayor(5, 3) == 5
assert mayor(2, 8) == 8

# Casos borde
assert mayor(0, 0) == 0
assert mayor(-1, -5) == -1

#Errores esperados
assert mayor("a", 5)  # Esto debería fallar
