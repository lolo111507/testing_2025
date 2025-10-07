# ejercicio_2_2.py
"""
Mejora el validador de email combinando ASSERT y TRY/EXCEPT
"""

def validar_email_completo(email):
    try:
        # TU CÓDIGO AQUÍ - Agrega asserts para:
        # - Email no vacío
        # - Debe contener '@'
        # - Debe tener un dominio (contener '.' después del '@')
        
        # Verifica que no haya espacios
        assert ' ' not in email, "El email no puede contener espacios"
        
        print(f"✅ Email válido: {email}")
        return True
        
    except AssertionError as e:
        print(f"❌ Email inválido: {e}")
        return False

# Pruebas:
if __name__ == "__main__":
    print("📧 Probando validador de email:")
    
    validar_email_completo("usuario@email.com")      # ✅ Válido
    validar_email_completo("usuario@email")          # ❌ Sin dominio
    validar_email_completo("usuario email.com")      # ❌ Con espacio
    validar_email_completo("")                       # ❌ Vacío
    validar_email_completo("usuarioemail.com")       # ❌ Sin '@'
    validar_email_completo("usuario@.com")          # ❌ Dominio inválido