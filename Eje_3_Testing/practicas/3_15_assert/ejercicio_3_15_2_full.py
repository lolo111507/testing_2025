# ejercicio_3_15_2_full.py
"""
Programa completo para calcular IMC.
- Contiene la función calcular_imc(peso, altura) con asserts para validación.
- Permite ejecución por línea de comandos: python ejercicio_3_15_2_full.py <peso> <altura>
- Si no recibe argumentos, solicita entrada interactiva.
"""

import sys
import math


def calcular_imc(peso, altura):
    """Calcula el IMC con validaciones.

    Args:
        peso: peso en kilogramos (int o float)
        altura: altura en metros (int o float)

    Returns:
        imc (float)
    """
    assert isinstance(peso, (int, float)), "El peso debe ser un número"
    assert isinstance(altura, (int, float)), "La altura debe ser un número"
    assert 0 < peso < 300, "Peso debe ser > 0 y < 300 kg"
    assert 0 < altura < 3, "Altura debe ser > 0 y < 3 metros"

    imc = peso / (altura ** 2)

    assert math.isfinite(imc) and imc > 0, "IMC debe ser un número positivo y finito"

    return imc


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]

    if len(argv) >= 2:
        try:
            peso = float(argv[0])
            altura = float(argv[1])
        except ValueError:
            print("Error: argumentos inválidos. Usa: python ejercicio_3_15_2_full.py <peso> <altura>")
            return 1
    else:
        try:
            peso = float(input("Introduce el peso en kg: "))
            altura = float(input("Introduce la altura en metros: "))
        except Exception as e:
            print(f"Entrada inválida: {e}")
            return 1

    try:
        imc = calcular_imc(peso, altura)
    except AssertionError as e:
        print(f"Error de validación: {e}")
        return 1

    print(f"✅ IMC calculado: {imc:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
