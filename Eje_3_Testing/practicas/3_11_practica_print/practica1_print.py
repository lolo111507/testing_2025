def contar_caracteres(frase):
    """
    Cuenta cuántas letras tiene la palabra.
    ERROR intencional: olvida contar espacios y guiones.
    """
    contador = 0
    for letra in frase:
        print(f"[DEBUG] letra actual: '{letra}'")   # print intermedio
        if letra.isalpha():
            contador += 1
        print(f"[DEBUG] contador parcial: {contador}")  # print intermedio
    return contador

# Ejemplos para probar
mi_frase = "Escuela Proa-2025"

#for p in palabras:
print("Caracteres contados:", contar_caracteres(mi_frase))  # Esperado: 4
