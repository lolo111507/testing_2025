# Tipos de errores en programación

En esta actividade veremos tres tipos principales de errores que se presentan en Python (y en la mayoría de los lenguajes de programación).

---

## 1. Errores de Sintaxis
Son errores que impiden que el código se ejecute porque la estructura no es válida.
Ejemplo:
```python
def saludo(nombre)
    print("Hola,", nombre)
```
Error: falta el `:` en la definición de la función.

---

## 2. Errores en Tiempo de Ejecución
El código está bien escrito, pero falla cuando se ejecuta.
Ejemplo:
```python
lista = [1, 2, 3]
print(lista[5])  # índice fuera de rango
```

---

## 3. Errores Lógicos
El programa corre, pero el resultado no es el esperado.
Ejemplo:
```python
def promedio(numeros):
    return sum(numeros)  # falta dividir por la cantidad
```

---

## Actividad en clase
- Ejecutar cada script con errores.
- Identificar el tipo de error (sintaxis, ejecución, lógico).
- Probar una solución y verificar que funcione.
- Comparar con la versión corregida.

---

## Recursos recomendados
- [Python Oficial - Errores y excepciones](https://docs.python.org/es/3/tutorial/errors.html)
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)
- [W3Schools - Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

---

✅ **Fallar es normal en programación**, y que el valor está en saber **detectar, clasificar y corregir** errores.
