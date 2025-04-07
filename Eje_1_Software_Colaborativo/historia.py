
import random

def mi_fun():
    
    personajes = ["un mago", "una princesa", "un dragón", "un astronauta", "un pitufo"]
    lugares = ["un castillo", "el bosque", "el espacio", "una isla", "un bar"]
    verbos = ["corrió", "voló", "luchó", "exploró", "robó"]
    adjetivos = ["mágico", "peligroso", "gigante", "misterioso"]

    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    verbo = random.choice(verbos)
    adjetivo = random.choice(adjetivos)

    texto = f"Había una vez {personaje} que {verbo} a través de {lugar} {adjetivo}."
    return texto

print(mi_fun())