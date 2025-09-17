# Script 3: Juego de puntos
def juego_puntos():
    puntos = 0
    for i in range(5):
        # Error: el incremento es incorrecto
        puntos = puntos + 0
    return puntos

print("Puntaje final:", juego_puntos())  # Esperado: 5
