# Repaso Try/Except
https://ellibrodepython.com/excepciones-try-except-finally


# Pruebas automáticas con `assert` en Python
---

## **Objetivos**

* Comprender el propósito del uso de `assert` para validar resultados automáticamente.
* Incorporar el uso de `assert` dentro de scripts para detectar errores lógicos.
* Diferenciar pruebas correctas y fallidas interpretando los mensajes de error del intérprete.

---

**¿Qué es `assert`?**

- Palabra clave de Python para verificar que una condición sea verdadera
- Sintaxis: `assert condición, "mensaje_de_error"`
- Si la condición es `True`: el programa continúa normalmente
- Si la condición es `False`: se lanza una excepción `AssertionError`

* `assert` es una **verificación interna del código**: una expresión que **debe ser verdadera** para continuar la ejecución (Si la condición es `True`: el programa continúa normalmente).
* Si la condición es `False`, Python lanza una **AssertionError** y detiene el programa.

* Se usa principalmente en:

  * Comprobaciones rápidas durante el desarrollo.
  * Validaciones de entrada o cálculos intermedios.
  * Mini-tests automáticos integrados en los scripts.

**Sintaxis:**

```python
assert condición, "mensaje de error opcional"
```

---

## **Ejemplo introductorio**

```python
def promedio(lista):
    assert len(lista) > 0, "La lista no puede estar vacía"
    return sum(lista) / len(lista)

print(promedio([10, 20, 30]))   # OK
print(promedio([]))             # Falla con AssertionError
```

Si ejecutás este código, el segundo `print()` genera:

```
AssertionError: La lista no puede estar vacía
```

---

## **Reflexión final**

> Los asserts son **la forma más simple de automatizar pruebas** sin usar frameworks.
> Permiten construir una primera capa de control antes de pasar a testing estructurado con `unittest` o `pytest`.

---

## 📚 **Recursos externos**

* 📖 [Documentación oficial de `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
* 🎥 [Video – “Assert en Python explicado fácil”](https://www.youtube.com/watch?v=I_g4Y3sSZ50)

---

**¿Cómo se relaciona con try/except?**
- `assert`: Verificación proactiva - "esto DEBERÍA ser verdad"
- `try/except`: Manejo reactivo - "si algo sale mal, haz esto"
- `raise` es la palabra clave en Python para generar o lanzar excepciones manualmente. Mientras que assert verifica condiciones, raise te permite crear excepciones cuando tú quieras.
- Son complementarios, no excluyentes

### **Diferencias clave**

| Assert | Try/Except |
|--------|------------|
| Para condiciones que SIEMPRE deben ser verdaderas | Para manejar errores esperados |
| Debugging y desarrollo | Producción y manejo de errores |
| Se puede deshabilitar con `-O` | Siempre activo |

## **Parte Práctica**

### **Actividad 1: Juego "Adivina el Número" con Assert** (25 minutos)

**Script base del juego (sin clases):**
```python
import random

def inicializar_juego(rango_min=1, rango_max=100):
    """Inicializa el juego y retorna el estado del juego"""
    assert rango_min < rango_max, "El mínimo debe ser menor al máximo"
    
    return {
        'rango_min': rango_min,
        'rango_max': rango_max,
        'numero_secreto': random.randint(rango_min, rango_max),
        'intentos': 0,
        'max_intentos': 7
    }

def adivinar_numero(juego, numero_usuario):
    """Verifica si el número del usuario es correcto"""
    # TODO: Agregar assert para validar que el número esté en el rango
    # TODO: Agregar assert para validar intentos restantes
    
    juego['intentos'] += 1
    
    if numero_usuario == juego['numero_secreto']:
        return "¡Correcto! Ganaste."
    elif numero_usuario < juego['numero_secreto']:
        return "Muy bajo. Intenta con un número mayor."
    else:
        return "Muy alto. Intenta con un número menor."

def jugar_adivina_numero():
    """Función principal del juego"""
    juego = inicializar_juego(1, 50)
    
    print(f" Adivina el número entre {juego['rango_min']} y {juego['rango_max']}")
    print(f"Tienes {juego['max_intentos']} intentos")
    
    while juego['intentos'] < juego['max_intentos']:
        try:
            guess = int(input("Tu adivinanza: "))
            resultado = adivinar_numero(juego, guess)
            print(resultado)
            
            if "Ganaste" in resultado:
                print(f"¡Felicidades! Lo lograste en {juego['intentos']} intentos")
                break
                
            intentos_restantes = juego['max_intentos'] - juego['intentos']
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intentos")
            else:
                print(f"¡Game Over! El número era {juego['numero_secreto']}")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except AssertionError as e:
            print(f"⚠️  Error de validación: {e}")

# Pruebas unitarias con assert
def test_juego_adivina():
    """Función de testing con asserts"""
    print("🔍 Ejecutando pruebas del juego...")
    
    # Test 1: Validación de rango inválido
    try:
        inicializar_juego(100, 1)
        assert False, "Debería haber fallado con rango inválido"
    except AssertionError as e:
        assert "mínimo debe ser menor" in str(e)
        print("✅ Test 1 pasado: Rango inválido detectado")
    
    # Test 2: Juego válido se crea correctamente
    juego = inicializar_juego(1, 10)
    assert juego['rango_min'] == 1
    assert juego['rango_max'] == 10
    assert 1 <= juego['numero_secreto'] <= 10
    print("✅ Test 2 pasado: Juego creado correctamente")
    
    # Test 3: Lógica de adivinanza - número correcto
    juego_test = {
        'rango_min': 1,
        'rango_max': 10,
        'numero_secreto': 5,
        'intentos': 0,
        'max_intentos': 7
    }
    
    resultado = adivinar_numero(juego_test, 5)
    assert "Ganaste" in resultado
    assert juego_test['intentos'] == 1
    print("✅ Test 3 pasado: Adivinanza correcta funciona")
    
    # Test 4: Lógica de adivinanza - número bajo
    juego_test['intentos'] = 0  # Reiniciar intentos
    resultado = adivinar_numero(juego_test, 3)
    assert "bajo" in resultado.lower()
    print("✅ Test 4 pasado: Número bajo detectado")
    
    # Test 5: Lógica de adivinanza - número alto
    juego_test['intentos'] = 0  # Reiniciar intentos
    resultado = adivinar_numero(juego_test, 7)
    assert "alto" in resultado.lower()
    print("✅ Test 5 pasado: Número alto detectado")

# Ejemplo de asserts en funciones de cálculo
def calcular_descuento(precio, porcentaje_descuento):
    """Calcula el precio con descuento con validaciones"""
    assert precio >= 0, "El precio no puede ser negativo"
    assert 0 <= porcentaje_descuento <= 100, "El descuento debe estar entre 0 y 100"
    
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    
    assert precio_final >= 0, "El precio final no puede ser negativo"
    return precio_final

def test_calculo_descuento():
    """Pruebas para la función de descuento"""
    print("\n🔍 Probando función de descuento...")
    
    # Test válido
    resultado = calcular_descuento(100, 20)
    assert resultado == 80
    print("✅ Cálculo de descuento correcto")
    
    # Test con descuento inválido
    try:
        calcular_descuento(100, 150)
        assert False, "Debería haber fallado"
    except AssertionError:
        print("✅ Descuento inválido detectado")
    
    # Test con precio negativo
    try:
        calcular_descuento(-50, 10)
        assert False, "Debería haber fallado"
    except AssertionError:
        print("✅ Precio negativo detectado")

if __name__ == "__main__":
    # Ejecutar pruebas primero
    test_juego_adivina()
    test_calculo_descuento()
    
    print("\n" + "="*50)
    print("🎯 ¡Todo listo para jugar!")
    print("="*50 + "\n")
    
    # Jugar el juego
    jugar_adivina_numero()
```

### **Ejercicios Prácticos** (17 minutos)

**Ejercicio 1: Completar las validaciones en adivinar_numero** (7 minutos)
```python
def adivinar_numero(juego, numero_usuario):
    """Verifica si el número del usuario es correcto"""
    # TODO 1: Validar que el número esté dentro del rango permitido
    # assert condición, "El número debe estar entre X y Y"
    
    # TODO 2: Validar que no hayamos excedido el máximo de intentos
    # assert condición, "No hay más intentos disponibles"
    
    juego['intentos'] += 1
    
    if numero_usuario == juego['numero_secreto']:
        return "¡Correcto! Ganaste."
    elif numero_usuario < juego['numero_secreto']:
        return "Muy bajo. Intenta con un número mayor."
    else:
        return "Muy alto. Intenta con un número menor."
```

**Ejercicio 2: Crear función con validaciones** (5 minutos)
```python
def crear_perfil_usuario(nombre, edad, email):
    """
    Crea un perfil de usuario con validaciones usando assert
    Reglas:
    - nombre: no vacío, máximo 50 caracteres
    - edad: entre 13 y 120 años
    - email: debe contener '@'
    """
    # TODO: Agregar asserts para validar cada parámetro
    
    return {
        'nombre': nombre,
        'edad': edad,
        'email': email
    }

# Prueba la función
def test_perfil_usuario():
    print("\n🔍 Probando creación de perfiles...")
    
    # Perfil válido
    perfil = crear_perfil_usuario("Ana", 25, "ana@email.com")
    assert perfil['nombre'] == "Ana"
    print("✅ Perfil válido creado")
    
    # TODO: Probar perfiles inválidos y verificar que los asserts fallen
```

**Ejercicio 3: Debugging con VS Code** (5 minutos)
1. Colocar breakpoints en los asserts de `adivinar_numero`
2. Ejecutar en modo debug (F5)
3. Probar con números fuera de rango y observar el AssertionError
4. Usar la consola de debug para inspeccionar variables

---

## **Soluciones a los Ejercicios**

**Solución Ejercicio 1:**
```python
def adivinar_numero(juego, numero_usuario):
    """Verifica si el número del usuario es correcto"""
    # Validación de rango
    assert juego['rango_min'] <= numero_usuario <= juego['rango_max'], \
        f"El número debe estar entre {juego['rango_min']} y {juego['rango_max']}"
    
    # Validación de intentos
    assert juego['intentos'] < juego['max_intentos'], \
        f"No hay más intentos disponibles (máximo: {juego['max_intentos']})"
    
    juego['intentos'] += 1
    
    if numero_usuario == juego['numero_secreto']:
        return "¡Correcto! Ganaste."
    elif numero_usuario < juego['numero_secreto']:
        return "Muy bajo. Intenta con un número mayor."
    else:
        return "Muy alto. Intenta con un número menor."
```

**Solución Ejercicio 2:**
```python
def crear_perfil_usuario(nombre, edad, email):
    """
    Crea un perfil de usuario con validaciones usando assert
    """
    assert nombre and len(nombre.strip()) > 0, "El nombre no puede estar vacío"
    assert len(nombre) <= 50, "El nombre no puede tener más de 50 caracteres"
    assert 13 <= edad <= 120, "La edad debe estar entre 13 y 120 años"
    assert '@' in email, "El email debe contener '@'"
    
    return {
        'nombre': nombre.strip(),
        'edad': edad,
        'email': email
    }

def test_perfil_usuario():
    print("\n🔍 Probando creación de perfiles...")
    
    # Perfil válido
    perfil = crear_perfil_usuario("Ana", 25, "ana@email.com")
    assert perfil['nombre'] == "Ana"
    print("✅ Perfil válido creado")
    
    # Probar nombre vacío
    try:
        crear_perfil_usuario("", 25, "test@email.com")
        assert False, "Debería haber fallado"
    except AssertionError:
        print("✅ Nombre vacío detectado")
    
    # Probar edad inválida
    try:
        crear_perfil_usuario("Juan", 10, "test@email.com")
        assert False, "Debería haber fallado"
    except AssertionError:
        print("✅ Edad inválida detectada")
    
    # Probar email sin @
    try:
        crear_perfil_usuario("Maria", 30, "email-invalido")
        assert False, "Debería haber fallado"
    except AssertionError:
        print("✅ Email inválido detectado")
```

---

### **Resumen de aprendizajes:**
-  `assert` es como un "guardián" que verifica condiciones importantes
-  Los mensajes claros en asserts ayudan a entender rápidamente el problema
-  Son ideales para desarrollo y debugging
-  Complementan el manejo de errores con try/except

### **Próximos pasos sugeridos:**
- Experimentar con el modo optimizado de Python: `python -O script.py`
