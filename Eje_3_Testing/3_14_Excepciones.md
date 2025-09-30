## Manejo de Excepciones 

https://www.youtube.com/watch?v=KG7QBTvFf8M

Las **excepciones** son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de las instrucciones. No son necesariamente errores de sintaxis (que impiden que el código se ejecute), sino situaciones inesperadas (como que el usuario ingrese texto en lugar de un número, o que un archivo no exista).

El objetivo del manejo de excepciones es hacer que tu código sea **robusto** (que no se "cuelgue" o falle inesperadamente). El manejo de excepciones consiste basicamente en:

1.  **Intentar** ejecutar código que podría fallar (`try`).
2.  **Capturar** y responder al fallo de forma controlada (`except`).
3.  **Continuar** la ejecución del programa en lugar de terminar abruptamente.

El bloque principal para esto es el **`try...except`**:

  * **`try`**: Contiene el código "riesgoso" que podría generar una excepción.
  * **`except`**: Contiene el código que se ejecuta *solo si* ocurre la excepción especificada en el bloque `try`.

-----

## Ejemplo Práctico en Python

Imaginemos que le pedimos a un usuario un número y luego lo usas para dividir. Si el usuario introduce un cero, se produce la excepción `ZeroDivisionError`.

### ❌ Programa Sencillo SIN Manejo de Excepciones

Este código fallará si el usuario introduce un `0` o cualquier texto (porque `int()` también fallaría).

```python
# Código sin manejo de excepciones
num = int(input("Introduce un número entero: "))
resultado = 100 / num
print(f"El resultado es: {resultado}")

# Si el usuario introduce '0', el programa CRASHEA y muestra:
# ZeroDivisionError: division by zero
```

### ✅ Programa Sencillo CON Manejo de Excepciones

Aquí el programa "sabe" qué hacer si ocurre el error, evitando el fallo.

```python
# Código con manejo de excepciones
try:
    # 1. Código "riesgoso"
    num_str = input("Introduce un número entero (¡no puede ser cero!): ")
    num = int(num_str)
    
    resultado = 100 / num
    
except ZeroDivisionError:
    # 2. Se ejecuta si se divide por cero
    print("¡Error! No puedes dividir por cero. Inténtalo de nuevo.")
    
except ValueError:
    # 3. Se ejecuta si el input no se puede convertir a entero (ej: el usuario escribe "hola")
    print("¡Error! Debes introducir un número entero válido, no texto.")

except Exception as e:
    # 4. Bloque genérico para cualquier otra excepción no prevista
    print(f"Ocurrió un error inesperado: {e}")
    
else:
    # 5. Opcional: Se ejecuta SÓLO si NO hubo excepciones
    print(f"¡Éxito! El resultado es: {resultado}")
    
finally:
    # 6. Opcional: Se ejecuta SIEMPRE, haya o no excepción (útil para limpieza)
    print("Fin del intento de cálculo.")

```

-----

## Ejercicio Propuesto

Crear una función para leer datos de un archivo e imprimirlos en pantalla.

**Requisito:** Pedir al usuario el nombre de un archivo de texto (txt). Intenta abrir y leer su contenido e imprimir el contenido.  Si el archivo no existe, el programa debe informarlo y NO debe fallar.

### Pistas

1.  Usa el bloque **`try`** para la operación de abrir el archivo: `f = open(nombre_archivo, 'r')`.
2.  La excepción que se lanza cuando un archivo no existe se llama **`FileNotFoundError`**.
3.  Usa un bloque **`except FileNotFoundError:`** para capturar ese error e imprimir un mensaje amigable.
4.  Utiliza el bloque **`finally`** para asegurarte de que, si el archivo se abrió correctamente, siempre se cierre con `f.close()`.

/*
<!--**(extra : La clave está en definir la variable `f` antes del `try` a `None` para poder verificar si se abrió o no dentro del `finally`).**-->