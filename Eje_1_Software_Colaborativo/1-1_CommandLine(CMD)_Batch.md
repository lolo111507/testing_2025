### _Qué es el CMD?_

El Símbolo del sistema, también llamado CMD ( por la contracción de la palabra __**C**o**M**man**D**__), forma parte de Windows y no puede ser desinstalado. Es una herramienta que, mediante comandos, permite realizar acciones avanzadas. Si bien puede parecer a la Terminal de GNU/Linux, el CMD no es tan potente.

A continuación se proporcionas los comandos más comunes usados en Windows y sus homólogos en Linux.ones.

**TABLA DE COMANDOS SIMILARES ENTRE WINDOWS Y LINUX**

| Propósito | WINDOWS | LINUX | Ejemplo básico de LINUX |
|----|----|----|----|
| Ayuda sobre comandos | cmd /? | man cmd | man comando |
| Crear un directorio | mkdir |mkdir| mkdir /home/qdirectorio |
| Cambia a un directorio | cd |cd | cd /home/qdirectorio |
| Sube un directorio | cd .. | cd .. | |
| Lista directorio | dir | ls -ls| |
| Borra la pantalla | cls | clear| |
| Cierra la ventana | exit |exit| |
| Borrar un directorio | rmdir | rmdir | rmdir /home/qdirectorio |
| Muestra un archivo | more | more | more qfichero |
| Renombra un archivo | rename | mv | mv nombreold nombrenew |
| Copia archivos | copy | cp | cp qfichero.txt /home/qdirectorio |
| Mueve archivos | move | mv | mv qfichero.txt /home/qdirectorio |
| Muestra o conf fecha | date | date| |
| Muestra o conf hora | time | date| |
| Borra archivos| del | rm | rm qfichero.txt |
| Busca texto en archivo | find | grep | grep “que contenido” qfichero.txt |
| Crea un archivo | copy con | touch | touch newfichero.txt |
| Visualiza la salida std | echo | echo | echo Testing_QA_CUAC |
____

Para mas detalles sobre los comando basicos de CMD, leer: https://www.xataka.com/basics/comandos-basicos-para-dar-tus-primeros-pasos-consola-windows-cmd


**Ejercicio 1:**

  1. En tu computadora crea, desde el terminal (Run.. "cmd"), una carpeta llamada "temp2025" en la dirección C:\
        mkdir C:\temp2025

**Ejercicio 2:** - Creación de carpetas y archivos por línea de comandos.  
    
 1.  Comandos cd, mkdir, dir, tree: Crear el sig. arbol de directorios y listalo en pantalla.

```
     C:\temp2025\
			|- Testing\
				|- eje1-SofwareColaborativo
				|- eje2-RedesDeDatos
				|- eje3-TestingQA
			|- Programacion4
			|- AppDev
```

2. Comando type: Crear 1 archivos ejeX-readme.txt, en cada una de las carpetas de los ejes (reamplazando la X por el número de eje Correspondiente). 

     Utilizar el comando: `tree C:\temp2025\ /F`  para listar el arból de directorio y los archivos creados. 
	
 3. Comando notepad:	editar cada uno de los archivos txt creado y como contenido en cada archivo, leer y copiar lo que refiere a cada eje en https://github.com/lole-s/testing_2025/blob/main/Dise%C3%B1oCurricular.md


 ### Batch! Bash!. 
 
	Un archivo Batch en Windows es un archivo de texto que contiene una serie de comandos que se ejecutan en la línea de comandos. Estos archivos tienen una extensión .bat o .cmd y se utilizan para automatizar tareas repetitivas o realizar secuencias de comandos de manera eficiente.
 
	Bash (Bourne Again Shell) es un intérprete de comandos utilizado en sistemas Unix y Unix-like, como Linux y macOS. A diferencia de los archivos Batch en Windows, los scripts Bash se ejecutan en una terminal y pueden contener comandos mucho más avanzados y potentes para la administración del sistema y la automatización de tareas. Los archivos de script Bash suelen tener una extensión .sh.

	En resumen, mientras que Batch es específico de Windows, Bash es más común en sistemas Unix y ofrece mayor flexibilidad y potencia para scripts y automatización
	
#### Lista de Comandos Batch  

Lista de algunos de los comandos más comunes y útiles en Batch, organizados por categorías:

* **`cd` (Change Directory):** Cambia el directorio actual.
* **`dir` (Directory):** Lista los archivos y carpetas en un directorio.
* **`mkdir` (Make Directory):** Crea una nueva carpeta.
* **`rmdir` (Remove Directory):** Elimina una carpeta vacía.
* **`del` (Delete):** Elimina uno o más archivos.
* **`copy`:** Copia archivos de una ubicación a otra.
* **`move`:** Mueve archivos o carpetas.
* **`ren` (Rename):** Cambia el nombre de un archivo o carpeta.
* **`type`:** Muestra el contenido de un archivo de texto.
* **`attrib`:** Cambia los atributos de un archivo (lectura, oculto, etc.).

**Gestión del sistema:**

* **`cls` (Clear Screen):** Limpia la pantalla de la consola.
* **`date`:** Muestra o establece la fecha del sistema.
* **`time`:** Muestra o establece la hora del sistema.
* **`tasklist`:** Muestra los procesos en ejecución.
* **`taskkill`:** Termina un proceso en ejecución.
* **`shutdown`:** Apaga o reinicia el equipo.
* **`ipconfig`:** Muestra la configuración de red IP.
* **`ping`:** Comprueba la conectividad de red con otro equipo.

**Flujo de control y lógica:**

* **`echo`:** Muestra un mensaje en la consola.
* **`@echo off`:** Desactiva la visualización de los comandos en la consola.
* **`pause`:** Detiene la ejecución del script y espera a que el usuario presione una tecla.
* **`if`:** Ejecuta un comando condicionalmente.
* **`for`:** Ejecuta un comando repetidamente.
* **`goto`:** Salta a una etiqueta específica dentro del script.
* **`call`:** Llama a otro script Batch desde el script actual.
* **`exit`:** Sale del script Batch o de la consola.
* **`rem` (Remark):** Permite añadir comentarios en el script.
* **`set`:** Muestra, establece o elimina variables de entorno.

**Redirección y tuberías:**

* **`>`:** Redirige la salida de un comando a un archivo.
* **`>>`:** Anexa la salida de un comando a un archivo.
* **`<`:** Redirige la entrada de un comando desde un archivo.
* **`|` (Pipe):** Envía la salida de un comando como entrada a otro comando.

**Otros comandos útiles:**

* **`assoc`:** Muestra o modifica las asociaciones de extensiones de archivos.
* **`find`:** Busca una cadena de texto dentro de un archivo.
* **`findstr`:** Busca cadenas de texto en archivos.
* **`help`:** Muestra información de ayuda sobre un comando.
* **`ver`:** Muestra la versión del sistema operativo.

**Puntos importantes:**

* Esta lista no es exhaustiva, pero incluye los comandos más utilizados.
* Puedes obtener ayuda sobre un comando específico escribiendo `help nombre_del_comando` en la consola.
* Algunos comandos pueden tener opciones y parámetros adicionales que modifican su comportamiento.
* Es importante recordar que algunos comandos pueden variar ligeramente dependiendo de la versión de Windows que se esté utilizando.

#### Ejemplo Batch!

El siguiente ejemplo de un script batch que incluye una estructura `IF` para tomar decisiones basadas en la entrada del usuario.

Este script batch pedirá al usuario que ingrese un número y luego verificará si el número es mayor, menor o igual a 10.

```batch
@echo off
:: Desactiva la visualización de los comandos en la pantalla

set /p num=Ingresa un numero: 
:: Pide al usuario que ingrese un número y lo guarda en la variable 'num'

if %num% GTR 10 (
    echo El numero es mayor que 10.
) else if %num% LSS 10 (
    echo El numero es menor que 10.
) else if %num% EQU 10 (
    echo El numero es igual a 10.
)
:: Verifica si el número ingresado es mayor (GTR: Es la abreviatura de "Greater Than" (Mayor Que)), menor (LSS: Es la abreviatura de "Less Than" (Menor Que)) o igual (EQU, que significa "Equal" (Igual)) a 10 y muestra el mensaje correspondiente

pause
:: Pausa la ejecución del script para que el usuario pueda ver el resultado antes de que la ventana se cierre
```
Guarda este script en un archivo con extensión `.bat`, por ejemplo, `verificar_numero.bat`, y ejecútalo para ver cómo funciona.

####

**Ejercicio 3** Investigar y crear archivo BATCH (hora.bat) que muestre por consola la fecha y hora actual. 

**Ejercicio 4** Investigar y crear archivo BATCH (respaldo.bat) para respaldar automaticamente los archivos *txt* creados en el ejercicio 2. Almacenar los respaldos en "C:\temp2025\backup"

**Ejercicio 5** Investigar y crear archivo BATCH (SeVemoEnDisney.bat) para lanzar el mensaje "Se vemo En Disney"  y una cuenta regresiva de 10 segundos que apague la PC. 

**Ejercicio 6** Investigar y modificar el archivo BATCH (`verificar_numero.bat`) del ejemplo para que controle que el usuario ingrese realemente un número y no otra cosa.
