# Introducción al Debugging (Depuración)

Cuando escribimos programas en Python (o en cualquier lenguaje), es **normal** que aparezcan errores:

* A veces el programa **se rompe** y no corre.
* Otras veces, corre pero **da un resultado incorrecto**.

**Depuración** significa:

1. Encontrar dónde está el problema.
2. Entender por qué ocurre.
3. Corregirlo.

---

## Herramientas para depurar

1. **Mensajes `print()`**

   * Mostrar valores de variables mientras el programa corre.
   * Ejemplo:

     ```python
     print("x =", x)
     ```

2. **Breakpoints (puntos de pausa)**

   * Parar el programa en una línea específica.
   * Revisar paso a paso qué está haciendo el código.

3. **Pensar analíticamente**

   * No se trata de adivinar, sino de **seguir pistas**: entradas, salidas, pasos intermedios.

---

## Importante:

* **Todos los programadores cometen errores.**
* Depurar es una **habilidad clave**: no se trata de escribir código perfecto, sino de saber **cómo arreglarlo rápido**.
* Aprender a **leer los errores** y **observar resultados inesperados** es parte del oficio.

---

# Depuración con `print`

## Objetivos
* Comprender cómo los **mensajes de salida** ayudan a detectar problemas.
* Aprender a **insertar `print()` estratégicamente**.
* Identificar valores inesperados en variables y flujos de ejecución.

---
### ¿Qué es depuración?
La depuración es el proceso de **encontrar y corregir errores** en un programa. 
Una de las formas más simples de hacerlo es con `print()`, mostrando valores en distintos momentos de la ejecución.

### Ventajas y limitaciones de `print()`
✅ Rápido, simple y siempre disponible.  
⚠️ Puede ensuciar el código si abusamos de él.  
⚠️ Es más difícil seguir programas grandes.

### Buenas prácticas con `print`
* Mostrar el **nombre y el valor** de la variable:
  ```python
  print("x =", x)
  ```
* Colocar prints en **condiciones y bucles** para ver qué ocurre.  
* **Eliminar los prints** antes de entregar el código.

---
#### hacer practica 3_11
