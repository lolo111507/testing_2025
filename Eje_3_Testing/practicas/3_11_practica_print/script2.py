# Script 2: Condicionales
def verificar_mayoria_edad(edad):
    # Error: debería aceptar 18 como mayor de edad
    if edad > 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

print(verificar_mayoria_edad(18))  # Esperado: mayor de edad
