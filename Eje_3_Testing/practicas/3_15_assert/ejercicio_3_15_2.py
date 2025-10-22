# ejercicio_3_15_2.py
# ejercicio_3_15_2.py
"""
Completa la función calcular_imc usando ASSERT
Reglas:
- Peso debe ser > 0 y < 300 kg
- Altura debe ser > 0 y < 3 metros
- IMC debe ser un número positivo
"""

import math


def calcular_imc(peso, altura):
    try:
        # Validaciones básicas con assert
        assert isinstance(peso, (int, float)), "El peso debe ser un número"
        assert isinstance(altura, (int, float)), "La altura debe ser un número"
        assert 0 < peso < 300, "Peso debe ser > 0 y < 300 kg"
        assert 0 < altura < 3, "Altura debe ser > 0 y < 3 metros"

        imc = peso / (altura ** 2)

        # Verificar que el IMC es un número positivo y finito
        assert isinstance(imc, (int, float)) and math.isfinite(imc), "IMC no es un número finito"
        assert imc > 0, "IMC debe ser un número positivo"

        print(f"✅ IMC calculado: {imc:.2f}")
        return imc
    except AssertionError as e:
        print(f"Error de validación: {e}")
        return 1


# Pruebas:
if __name__ == "__main__":
    print("⚖️ Probando calculadora de IMC:")

    #calcular_imc(70, 1.75)    # ✅ Debe funcionar
    #calcular_imc(-5, 1.75)  # ❌ Debe fallar
    calcular_imc(70, 0)     # ❌ Debe fallar