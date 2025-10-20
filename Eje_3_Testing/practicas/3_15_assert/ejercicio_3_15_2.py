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
    
    print(f"✅ IMC calculado: {imc:.2f} kg/m²")
    return imc

def calcular_peso(imc, altura):
    # TU CÓDIGO AQUÍ - Agrega asserts para validar peso y altura
    
    peso = imc*(altura ** 2)
    
    # TU CÓDIGO AQUÍ - Verifica que el IMC sea razonable
    
    print(f"✅ Peso calculado: {peso:.2f} Kg")
    return peso


# Pruebas:
if __name__ == "__main__":
    print("⚖️ Probando calculadora de IMC:")
    
    calcular_imc(110, 1.83)    # ✅ Debe funcionar
    # calcular_imc(-5, 1.75)  # ❌ Debe fallar
    # calcular_imc(70, 0)     # ❌ Debe fallar
#    calcular_peso(29.9, 1.83)   # ✅ Debe funcionar

""" 
Categoría               IMC (kg/m²)
Desnutrición		    < 18.5
Normal		            18,5 a 24,9
Sobrepeso		        25,0 a 29,9
Obesidad	I	        30,0 a 34,9
            II	        35,0 a 39,9
            III	        ≥ 40                    
Fuente: https://www.healthy-heart.org/es/mantenga-su-corazon-sano/mantener-un-peso-saludable/"""
