import sys


def main():
    nombre = sys.argv[1] if len(sys.argv) > 1 else input("Archivo: ")
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Archivo '{nombre}' no existe.")
    except Exception as e:
        print("Ocurrió un error:", e)


if __name__ == "__main__":
    main()
