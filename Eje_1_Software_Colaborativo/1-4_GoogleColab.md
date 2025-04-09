## Que es Google Colab


### [Blog sobre colab](https://www.hostgator.ar/blog/google-colab/)

### [Video Intro a Google COLAB](https://youtu.be/8VFYs3Ot_aA)

### [Bienvenido a Colab](https://colab.research.google.com/?hl=es)


#### **Ejercicio:** 

**Ejercicio 1: Mi primer notebook o cuaderno Colab!**

* **Objetivo**: Familiarizarse con la interfaz de Colab, crear un archivo, añadir texto y ejecutar código simple.

* **Pasos**:
    1.  **Crear un nuevo cuaderno**:
        * Abre Google Colab en tu navegador.
        * Haz clic en "Nuevo cuaderno".
    2.  **Añadir un título**:
        * En la parte superior del cuaderno, donde dice "UntitledX.ipynb", haz clic y escribe un título como "Mi primer cuaderno Colab - %TU NOMBRE%".
    3.  **Añadir una celda de texto**:
        * Haz clic en el botón "+ Texto" para crear una celda de texto.
        * Escribe un mensaje de bienvenida, por ejemplo: "¡Hola! Este es mi primer cuaderno en Colab. ¡Estoy emocionado de aprender Python!".
        * Para que el texto aparezca de forma correcta, presiona el botón de play que aparece a la izquierda de la celda de texto.
    4.  **Añadir una celda de código**:
        * Haz clic en el botón "+ Código" para crear una celda de código.
        * Escribe el siguiente código para imprimir un mensaje:

```python
print(" Testing PROA 2025!")
```

* Haz clic en el botón de "play" a la izquierda de la celda de código para ejecutarlo. Deberías ver el mensaje impreso debajo de la celda.
    5.  **Un pequeño cálculo**:
        * en la siguiente celda de código, escribe esto.

```python
print (2+2)
```

* Vuelve a presionar el botón de play, y veras el resultado de la operación.
* **Guardar el cuaderno**:
    * Colab guarda automáticamente tu trabajo, pero puedes ir a "Archivo" > "Guardar" para asegurarte.
    * Compartir el cuaderno a: jcsodo@escuelasproa.edu.ar


**Ejercicio 2: Calculando y graficando!!**

* **Objetivo**: Usar variables, obtener entrada del usuario, realizar cálculos sencillos, graficar los resultados y compartir el cuaderno.
* **Pasos**:
    1.  **Crear un nuevo cuaderno**:
        * Abre Google Colab en tu navegador.
        * Haz clic en "Nuevo cuaderno".
    2.  **Pedir la base y la altura del triángulo**:
        * Crea una celda de código.
        * Usa la función `input()` para pedir al usuario que ingrese la base del triángulo y almacénala en una variable llamada `base`.
        * Usa la función `input()` nuevamente para pedir la altura del triángulo y almacénala en una variable llamada `altura`.
        * Recuerda convertir las entradas a números decimales usando `float()`.
    3.  **Calcular el área**:
        * Crea otra celda de código.
        * Escribe la fórmula para calcular el área de un triángulo (base \* altura / 2) y almacena el resultado en una variable llamada `area`.
        * Usa la función `print()` para mostrar el resultado del área en la pantalla.
    4.  **Graficar el triángulo**:
        * Crea otra celda de código.
        * Importa la biblioteca `matplotlib.pyplot` usando `import matplotlib.pyplot as plt`.
        * Crea una lista de coordenadas `x` y `y` que representen los vértices del triángulo. Por ejemplo, `x = [0, base, 0]` y `y = [0, 0, altura]`.
        * Usa la función `plt.plot()` para graficar el triángulo.
        * Usa la función `plt.fill()` para rellenar el triángulo con color.
        * Usa la función `plt.show()` para mostrar la gráfica.
    5.  **Compartir el cuaderno**:
        * Haz clic en el botón "Compartir" en la esquina superior derecha.
        * En la ventana que aparece, escribe la dirección de correo electrónico "[dirección de correo electrónico eliminada]".
        * Asegúrate de que el permiso esté configurado como "Editor".
        * Haz clic en "Enviar".
    6.  **Colaboración en tiempo real**:
        * Pide a los alumnos que abran el cuaderno compartido entre dos compañeros.
        * Pídeles que agreguen celdas de texto con sus nombres y que escriban comentarios sobre el código del otro.
        * Anímalos a modificar el código juntos, por ejemplo, cambiando los colores del triángulo o agregando etiquetas a los ejes.

**adicionales**:

* Agregar un título a la gráfica usando la función `plt.title()`.
* Agregar etiquetas a los ejes usando las funciones `plt.xlabel()` y `plt.ylabel()`.


<!-- 
Solución 

```python
import matplotlib.pyplot as plt

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2

print("El área del triángulo es:", area)

# Definir las coordenadas de los vértices del triángulo
x = [0, base, 0]
y = [0, 0, altura]

# Graficar el triángulo
plt.plot(x, y)

# Rellenar el triángulo con color
plt.fill(x, y, color='skyblue')

# Agregar un título a la gráfica
plt.title("Área del triángulo")

# Agregar etiquetas a los ejes
plt.xlabel("Base")
plt.ylabel("Altura")

# Mostrar la gráfica
plt.show()
```
-->
