""" Ejercicio: Unit Test

Objetivo: Crear una función `calcular_descuento(precio, porcentaje)` 
que devuelva el precio final con descuento aplicado.

Instrucciones:
1. Crear la función que reciba dos parámetros:
   - `precio`: número positivo
   - `porcentaje`: número entre 0 y 100
2. Calcular el descuento y devolver el precio final.
3. Escribir al menos 4 tests unitarios usando `assert`:
   - Un caso normal (ej. 100 con 20%)
   - Un caso sin descuento
   - Un caso con 100% de descuento
   - Un caso con decimales
4. Ejecutar el script para verificar que todos los tests pasen.
5. (Opcional) Añadir tests para casos borde y errores esperados."""


# --- 1. FUNCIÓN A TESTEAR ---
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio final con descuento aplicado, redondeando a 2 decimales.
    :param precio: El precio original (número positivo).
    :param porcentaje: El porcentaje de descuento (número entre 0 y 100).
    :return: El precio final.
    """
    # Fórmula concisa: precio * (1 - porcentaje / 100)
    return round(precio * (1 - porcentaje / 100), 2)

# ----------------------------

# --- 2. TESTS UNITARIOS CON ASSERT ---
print("--- Ejecutando Tests Unitarios ---")
assert calcular_descuento(100, 20) == 80.00
assert calcular_descuento(30, 20) == 24.00
assert calcular_descuento(137, 5) == 130.15
assert calcular_descuento(220, 10) == 215.60

""" # 1. Caso normal (100 con 20% -> 80)
resultado_1 = calcular_descuento(100, 20)
assert resultado_1 == 80.00, f"Test 1 Falló: Esperado 80.00, Obtenido {resultado_1}"
print(f"Test 1 (Normal): OK ({resultado_1})")

# 2. Caso sin descuento (500 con 0% -> 500)
resultado_2 = calcular_descuento(500, 0)
assert resultado_2 == 500.00, f"Test 2 Falló: Esperado 500.00, Obtenido {resultado_2}"
print(f"Test 2 (Sin Descuento): OK ({resultado_2})")

# 3. Caso 100% de descuento (99.99 con 100% -> 0)
resultado_3 = calcular_descuento(99.99, 100)
assert resultado_3 == 0.00, f"Test 3 Falló: Esperado 0.00, Obtenido {resultado_3}"
print(f"Test 3 (Descuento Total): OK ({resultado_3})")

# 4. Caso con decimales (123.45 con 15% -> 104.93)
resultado_4 = calcular_descuento(123.45, 15)
assert resultado_4 == 104.93, f"Test 4 Falló: Esperado 104.93, Obtenido {resultado_4}"
print(f"Test 4 (Con Decimales): OK ({resultado_4})")

# 5. (Opcional) Caso borde: Precio 0
resultado_5 = calcular_descuento(0, 50)
assert resultado_5 == 0.00, f"Test 5 Falló: Esperado 0.00, Obtenido {resultado_5}"
print(f"Test 5 (Precio Cero): OK ({resultado_5})")

# -------------------------------------

print("\n✅ ¡Todos los tests pasaron exitosamente!") """