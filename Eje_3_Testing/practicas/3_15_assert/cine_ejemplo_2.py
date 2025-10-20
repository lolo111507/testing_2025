print("\n🎬 SISTEMA DE CINE - NIVEL 2: ASSERT + TRY/EXCEPT")

def verificar_edad_avanzado(edad_str):
    """Verifica edad manejando diferentes tipos de errores"""
    try:
        # Convertimos a número (puede fallar)
        edad = int(edad_str)
        
        # Validaciones con assert
        assert edad >= 0, "La edad no puede ser negativa"
        assert edad <= 120, "La edad no puede ser mayor a 120"
        
        # Lógica de negocio
        if edad >= 18:
            print(f"✅ Bienvenido! Tienes {edad} años - Puedes entrar")
            return True
        else:
            print(f"❌ Lo siento! Tienes {edad} años - No puedes entrar")
            return False
            
    except ValueError:
        print(f"❌ Error: '{edad_str}' no es un número válido")
        return False
    except AssertionError as e:
        print(f"⚠️  Error de validación: {e}")
        return False

# Pruebas
print("\n--- Casos con diferentes tipos de errores ---")
#verificar_edad_avanzado("25")     # ✅ Número válido +18
#verificar_edad_avanzado("15")     # ✅ Número válido -18
verificar_edad_avanzado("veinte") # ❌ Error de conversión
#verificar_edad_avanzado("-5")     # ❌ AssertionError
#verificar_edad_avanzado("150")    # ❌ AssertionError
