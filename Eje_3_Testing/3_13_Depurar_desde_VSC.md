#  Guía de depuración paso a paso (con Visual Studio Code)

## Objetivo

Aprender a **usar breakpoints** y las herramientas de depuración visual de VS Code para:

1. Seguir el flujo del programa.
2. Inspeccionar valores de variables.
3. Encontrar y corregir errores lógicos.

---

## 📝 Preparación

1. Abrir el script `3_13_practica_tienda.py` ubicado en la carpeta `practicas`. 

---

## 🚦 Paso 1: Configurar la depuración

1. En el menú lateral, hacé clic en el ícono de **depuración** (un insecto con un triángulo ▶).
2. Si VS Code te pide, creá un archivo `launch.json` con la opción:

   * **Python: Current File**.
3. Ahora vas a poder ejecutar con **F5**.

---

## Paso 2: Colocar Breakpoints

Hacé clic a la izquierda de la línea de código (en el margen, junto al número de línea).
Se te pone un **punto rojo 🔴**.

👉 Colocá breakpoints en:

* Línea del `if login(user, clave):` (para revisar el login).
* Dentro de `calcular_total` (donde suma `total`).
* Dentro de `aplicar_descuento`.

---

## 🔍 Paso 3: Iniciar la depuración

1. Presioná **F5**.
2. El programa se va a detener en el primer breakpoint.
3. Vas a ver arriba las opciones:

   * ▶ **Continue (F5)** → seguir hasta el próximo breakpoint.
   * ⬇ **Step Into (F11)** → entrar dentro de la función.
   * ↷ **Step Over (F10)** → ejecutar la línea sin entrar en funciones.
   * ⬆ **Step Out (Shift+F11)** → salir de la función.

---

## Paso 4: Detectar errores

###  1. Revisar Login

Verificar que el usuario pueda iniciar sesión solo si:

 * "ana" con clave "1234" 
 * "juan" con clave "abcd" 
Cualquier otra combinación ❌ debe dar error.
---

### 2. Revisar Subtotal

* Ingresar diferentes cantidades de productos y verificar los subtotales

---

###  3. Revisar Descuento por cliente

* "ana" → 20% de descuento
* "juan" → 10% de descuento
* Otros usuarios → sin descuento

---

## ✅ Resultado esperado

Al corregir, el programa debería mostrar:

```
=== Bienvenido a la tienda ===
✅ Login exitoso: ana
Subtotal: 350
Total con descuento: 280
```
* El caso de "Juan" como quedaría? 

## 🎥 Video recomendado

Un recurso visual, simple y entretenido para chicos de 16–18 años que ya saben un poco de Python:

👉 [Técnicas de Depuración (Debugging) en Python](https://www.youtube.com/watch?v=XTzUluo1e2o)
