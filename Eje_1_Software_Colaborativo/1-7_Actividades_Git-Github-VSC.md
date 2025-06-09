### Actividad 1 - Crear repo Nuevo

## 🧠 Objetivo del ejercicio

Aprender a:

1. Crear un repositorio local de Git.
2. Agregar archivos.
3. Hacer commits.
4. Crear un README.
5. Escribir un código simple.
6. Ver el historial de cambios (logs).
7. Crear y cambiar de rama (branch).
8. Hacer cambios en la nueva rama.

---

## 🧰 Requisitos previos

* Git instalado.
* Terminal o consola lista (Git Bash en Windows, Terminal en Linux/macOS).
* Un editor de texto como VSCode, Sublime Text o Notepad++ (o el Bloc de Notas).

---

## 📘 PASOS DEL EJERCICIO

### 1. Crear una carpeta para el proyecto

```bash
mkdir mi-primer-repo
cd mi-primer-repo
```

---

### 2. Inicializar un repositorio Git

```bash
git init
```

💡 Esto crea un repositorio vacío en tu carpeta.

---

### 3. Crear un archivo README

```bash
echo "# Mi Primer Proyecto Git" > README.md
```

👉 Este comando crea el archivo `README.md` con un título adentro.

---

### 4. Ver el estado del repositorio

```bash
git status
```

🔎 Git te va a decir que hay un archivo nuevo (`README.md`) sin trackear.

---

### 5. Agregar el archivo al área de staging

```bash
git add README.md
```

---

### 6. Hacer un commit

```bash
git commit -m "Agrego archivo README"
```

✅ Primer snapshot guardado.

---

### 7. Crear un archivo de código simple (ej: en Python)

```bash
echo "print('Hola mundo')" > hola.py
```

📁 Esto crea un archivo llamado `hola.py` con una línea de código.

---

### 8. Agregar y commitear el código

```bash
git add hola.py
git commit -m "Agrego script hola.py"
```

---

### 9. Ver historial de commits

```bash
git log
```

📜 Vas a ver una lista con los commits hechos, el autor, y el mensaje.

---

### 10. Crear una nueva rama (branch)

```bash
git branch nueva-idea
```

---

### 11. Cambiarte a esa nueva rama

```bash
git checkout nueva-idea
```

---

### 12. Hacer un cambio en esa rama

```bash
echo "print('Estoy en una nueva rama')" >> hola.py
git add hola.py
git commit -m "Modifico hola.py en nueva rama"
```

---

### 13. Ver las ramas existentes

```bash
git branch
```

🌱 La rama actual estará marcada con un asterisco (\*).

---

### 14. Volver a la rama principal (`main` o `master`)

```bash
git checkout main
```

👀 Si el repositorio se inicializó como `master`, usar `master` en vez de `main`.

---

### 15. Ver diferencia entre ramas (opcional)

```bash
git diff nueva-idea
```

📌 Te muestra qué cambios tiene la otra rama.

---

## ✅ BONUS: Combinar ramas

(Si querés ir más allá)

```bash
git merge nueva-idea
```

🎯 Esto trae los cambios de la otra rama a la principal.

---

## 📦 Resumen visual del flujo

```plaintext
Crea carpeta → git init → README.md → git add → git commit
hola.py → git add → git commit → git log
branch nueva → checkout → cambios → commit
checkout main → diff → merge (opcional)
```

---


<!--
## Clonar Repositorio desde Consola
1. clonar repositorio: https://github.com/fmendezy/Guia-de-Markdown
2. abrir repo desde consola.
3. ver logs
4. abrir repo de VSC
5. modificar archivo. ver VSC
6. crear rama en consola. 
7. ver rama en VSC

#### [Tutorial VSC](https://www.youtube.com/watch?v=CxF3ykWP1H4)

#### [Tutorial git en VSC](https://www.youtube.com/watch?v=qdec2M4NwT0)


## Crear repo desde VSC
1. Crear carpeta en el escritorio "MiRepoVSC"
2. Crear archivo "index.html"
3. Crear archivo "main.css"
4. Crear archivo "README.md"
5. Abrir proyecto en VSC. 
6. Inicializar repo de proyecto desde "Source Control"
7. Crear plantilla en "index.html"
8. Hacer add y commit
9. Publicar los cambios (la branch como proyecto publico)
10. Ir a GITHUB y verificar 



## Clonar Repositorio desde VSC

1. Abri VSC - Clonar https://github.com/lole-s/Testing-QA-CUAC
2. Ver Logs - Ver branchs
3. Ir  a Testing-QA-CUAC/Eje3-Testing/3-1_Intro.md y escribir en MarkDown el siguiente texto: 


-->