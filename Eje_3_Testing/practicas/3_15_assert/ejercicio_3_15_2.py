# ejercicio_3_15_2.py
"""
Completa la función calcular_imc usando ASSERT
Reglas:
- Peso debe ser > 0 y < 300 kg
- Altura debe ser > 0 y < 3 metros
- IMC debe ser un número positivo
"""

def calcular_imc(peso, altura):
    # TU CÓDIGO AQUÍ - Agrega asserts para validar peso y altura
    
    imc = peso / (altura ** 2)
    
    # TU CÓDIGO AQUÍ - Verifica que el IMC sea razonable
    
    print(f"✅ IMC calculado: {imc:.2f}")
    return imc

# Pruebas:
if __name__ == "__main__":
    print("⚖️ Probando calculadora de IMC:")
    
    calcular_imc(70, 1.75)    # ✅ Debe funcionar
    # calcular_imc(-5, 1.75)  # ❌ Debe fallar
    # calcular_imc(70, 0)     # ❌ Debe fallar
