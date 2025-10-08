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
