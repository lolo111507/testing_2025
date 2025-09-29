# Depuración con `pdb` y `breakpoint()`

## Objetivos
- Conocer el **debugger integrado de Python (`pdb`)**.
- Aprender a **pausar la ejecución con `breakpoint()`**.
- Usar comandos básicos para navegar en el código.

### ¿Qué es `pdb`?
`pdb` es el **depurador interactivo de Python**. Permite ejecutar el programa paso a paso,
revisar valores de variables y detener la ejecución en puntos específicos.

### Sintaxis básica
Para iniciar una sesión de depuración: 

```python
breakpoint()   # inicia depuración en ese punto
```
Cuando el programa llega a esa línea, entra en el **modo interactivo de depuración**.

### Comandos principales
- `n` → next (ejecuta siguiente línea)
- `s` → step (entra en función)
- `c` → continue (sigue hasta el próximo breakpoint)
- `q` → quit (salir)
- `p variable` → imprime el valor de una variable

### Comparación con `print`
- `print()` → rápido, útil, pero ensucia el código.
- `pdb` → más controlado y profesional, ideal para proyectos grandes.

## Recursos recomendados
- [Debugging in Python Docs](https://docs.python.org/3/library/pdb.html)
- [RealPython: Python Debugging](https://realpython.com/python-debugging-pdb/)


## PRACTICA
### 1. Factorial con error

Archivo: `factorial_error.py`

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 2)   #  Error: debería restar 1, no 2

print("Factorial de 5:", factorial(5))
```

Insertá `breakpoint()` dentro de la función y usá:

* `n` para avanzar línea por línea.
* `p n` para ver cómo va cambiando `n`.
* Identificá por qué el cálculo falla.

---

### 2. Bucle infinito

Archivo: `bucle_infinito.py`

```python
i = 0
while i < 5:
    print("i =", i)
    # ❌ Falta incrementar i
    # i += 1
```

👉 Insertá `breakpoint()` dentro del bucle.

* Usá `n` para avanzar.
* Revisá el valor de `i` con `p i`.
* Corregí el error.

---

### 3. Calculadora con funciones anidadas

Archivo: `calculadora.py`

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def calcular(x, y, operacion):
    if operacion == "suma":
        return restar(x, y)   # ❌ Error: llama a la función equivocada
    elif operacion == "resta":
        return sumar(x, y)
    else:
        return None

print("Resultado:", calcular(4, 2, "suma"))
```

👉 Insertá `breakpoint()` dentro de `calcular()`.

* Usá `s` para entrar en la función llamada.
* Descubrí qué función se ejecuta realmente.
* Corregí la lógica.



__ 
## NOTA: 


* **Antes de python 3.7** → había que `import pdb` y escribir `pdb.set_trace()`.
* **Desde 3.7** → con `breakpoint()` ya alcanza.


#### Ejemplo 1 — Usando `breakpoint()` (Python ≥ 3.7)

```python
def contar_letras(palabra):
    print("Voy a contar las letras de:", palabra)
    breakpoint()   # hace lo mismo que pdb.set_trace()
    return len(palabra)

print("Resultado:", contar_letras("hola"))
```

---

## Ejemplo2  — Usando `pdb.set_trace()` (Python < 3.7)

```python
import pdb

def contar_letras(palabra):
    print("Voy a contar las letras de:", palabra)
    pdb.set_trace()   # aquí el programa se detiene y entra al depurador
    return len(palabra)

print("Resultado:", contar_letras("hola"))
```

Cuando el código llega a `pdb.set_trace()`, se abre el modo interactivo `pdb`.

Se pueden usar comandos como:

* `n` → siguiente línea
* `c` → continuar
* `p palabra` → imprimir el valor de la variable

---


