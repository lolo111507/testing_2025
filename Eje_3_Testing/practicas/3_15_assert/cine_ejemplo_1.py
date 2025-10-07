# Ejercicio Escalonado: Sistema de Edad para Cine

## **Nivel 1: Assert Básico**

print("🎬 SISTEMA DE CINE - NIVEL 1: ASSERT BÁSICO")

def verificar_edad_basico(edad):
    """Verifica si una persona puede ver una película de +18"""
    assert edad >= 0, "La edad no puede ser negativa"
    assert edad <= 120, "La edad no puede ser mayor a 120"
    
    if edad >= 18:
        print(f"✅ Bienvenido! Tienes {edad} años - Puedes entrar")
        return True
    else:
        print(f"❌ Lo siento! Tienes {edad} años - No puedes entrar")
        return False

# Pruebas
print("\n--- Probando edades válidas ---")
verificar_edad_basico(20)  # ✅ Debe funcionar
verificar_edad_basico(16)  # ✅ Debe funcionar
verificar_edad_basico(-5)  # ❌ Debe fallar

try:
    verificar_edad_basico(150)  # ❌ Debe fallar
except AssertionError as e:
    print(f"Error esperado: {e}")
