"""
leer_archivo.py
Función para leer y mostrar el contenido de un archivo de texto con manejo de excepciones.
"""


def leer_y_mostrar(nombre_archivo: str) -> None:
    """Intenta abrir y leer un archivo de texto. Si no existe, informa y no lanza excepción.

    Args:
        nombre_archivo: Ruta o nombre del archivo a leer.
    """
    f = None
    try:
        f = open(nombre_archivo, "r", encoding="utf-8")
        contenido = f.read()
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    else:
        print("--- Contenido del archivo ---")
        print(contenido)
        print("--- Fin del contenido ---")
    finally:
        if f:
            try:
                f.close()
            except Exception:
                pass


if __name__ == "__main__":
    nombre = input("Introduce el nombre (o ruta) del archivo .txt a leer: ")
    leer_y_mostrar(nombre)
