# ejercicio_3_15_1.py
"""
Completa la función validar_contraseña usando ASSERT
Reglas que debe verificar:
1. La contraseña debe tener al menos 8 caracteres
2. Debe contener al menos un número
3. Debe contener al menos una letra mayúscula
"""

def validar_contraseña(contraseña):
    # TU CÓDIGO AQUÍ - Agrega los asserts necesarios
    # Pista: usa len(), any(), isdigit(), isupper()
    
    # Si pasa todas las validaciones
    print("✅ Contraseña válida!")
    return True

# Prueba tu función con estos casos:
if __name__ == "__main__":
    print("🔒 Probando validador de contraseñas:")
    
    # Debe funcionar
    validar_contraseña("Segura123")
    
    # Deben fallar:
    # validar_contraseña("corta")      # Muy corta
    # validar_contraseña("sololetras")   # Sin números
    # validar_contraseña("12345678")    # Sin mayúsculas