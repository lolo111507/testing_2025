# 🚀 Uso de Git y GitHub desde Visual Studio Code

## 🌐 ¿Qué es GitHub?

**GitHub** es una plataforma en línea para guardar y compartir código. Es como una red social para programadores, pero también una herramienta muy poderosa para colaborar, versionar y publicar proyectos.

GitHub usa **Git** (el sistema de control de versiones que ya conocés) para permitir que múltiples personas trabajen juntas en un mismo proyecto, de forma organizada y segura.

---

## 🧾 ¿Cómo crear una cuenta en GitHub?

1. Ingresá a: [https://github.com](https://github.com)
2. Hacé clic en el botón **Sign up**.
3. Completá los datos:
   - Nombre de usuario (único)
   - Email válido
   - Contraseña segura
4. Verificá tu cuenta por correo electrónico.
5. Elegí el plan **gratuito**.
6. ¡Listo! Ya tenés tu cuenta para empezar a usar GitHub.

> ✅ Recomendación: usá un correo que tengas acceso en clase para poder verificar rápidamente.

---

## 🎯 Objetivo de esta actividad

Aprender a trabajar con Git y GitHub desde **Visual Studio Code**, aprovechando las extensiones integradas y el control de versiones gráfico.

---

## 🧰 Requisitos previos

- Tener **Git instalado** en el sistema.
- Tener **Visual Studio Code** instalado.
- Tener cuenta en **GitHub** (ver instrucciones arriba).
- Tener configurado Git globalmente:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
````

---

## 🧩 Parte 1 – Configurar Visual Studio Code

### 1. Verificar que Git funcione

* Abrí Visual Studio Code.
* Abrí la terminal (`Ctrl + ñ`) y escribí:

  ```bash
  git --version
  ```

### 2. Instalar extensiones recomendadas

Desde el panel de extensiones (ícono de bloques), instalá:

| Extensión                         | ¿Para qué sirve?                         |
| --------------------------------- | ---------------------------------------- |
| ✅ GitHub Pull Requests and Issues | Ver y manejar PR sin salir de VSC        |
| ✅ GitLens                         | Ver quién escribió cada línea del código |
| ✅ Git Graph (opcional)            | Visualizar ramas y commits gráficamente  |

---

## 📂 Parte 2 – Crear un repositorio local con Git

1. Abrí una carpeta nueva desde `Archivo → Abrir carpeta`.
2. Andá al panel de control de versiones (ícono de rama).
3. Tocá **"Inicializar repositorio"**.
4. Creá un archivo `README.md` y escribí:

```markdown
# Mi primer proyecto con Git en Visual Studio Code
```

5. Escribí un mensaje de commit (ej: `Primer commit`) y confirmalo con ✔️.

---

## ☁️ Parte 3 – Subir tu proyecto a GitHub

### 1. Crear un nuevo repositorio

1. Ingresá a tu cuenta de [GitHub](https://github.com).
2. Hacé clic en **"New"** o "Nuevo repositorio".
3. Poné un nombre (por ejemplo: `mi-primer-repo-vsc`).
4. **No agregues README** (ya lo hiciste en tu compu).
5. Copiá la URL HTTPS del repositorio.

### 2. Conectar tu proyecto local al repositorio remoto

En la terminal integrada de VSC:

```bash
git remote add origin https://github.com/TU_USUARIO/mi-primer-repo-vsc.git   
# Agrega un “remoto” llamado origin que apunta a la URL de tu repositorio en GitHub.
#Así, tu repositorio local sabe a qué repositorio remoto debe conectarse para subir
#(push) o bajar (pull) cambios.

git branch -M main                                                          
# Renombra la rama actual a main. El parámetro -M fuerza el cambio de nombre, aunque
#la rama main ya exista. Es útil porque GitHub suele usar main como rama principal por defecto.

git push -u origin main                                                     
# Sube (push) la rama main de tu repositorio local al repositorio remoto origin
#(el que configuraste antes). El parámetro -u establece una relación de seguimiento
#entre tu rama local main y la rama main remota, para que en el futuro puedas usar
#simplemente git push o git pull sin especificar la rama.

```

---

## 🔄 Parte 4 – Subir y bajar cambios desde Visual Studio Code

### Subir cambios (Push) – Ejemplo

1. Hacé tus modificaciones.
  - Por ejemplo, creá un archivo llamado `testing.py` y agregá el siguiente código:

    ```python
    print("¡Hola, GitHub desde Visual Studio Code!")
    ```

2. Guardá el archivo.
3. En el panel de control de versiones, escribí un mensaje de commit, por ejemplo:  
  `Agrego archivo testing.py`
4. Confirmá el commit con el ✔️.
5. Tocá el botón **Push** o el icono de sincronizar 🔃 para subir los cambios a GitHub.
6. Verificar que los cambios se vean reflejados en el repositorio remoto de Github.

---

### Bajar cambios (Pull) – Ejemplo colaborativo

1. Ingresar a GitHub desde la web y:
  - Modificar el archivo `README.md` (por ejemplo, agregando su nombre, la fecha actual y el nombre de este espacio curricular).
  - Crear un archivo nuevo (por ejemplo, `saludo.py`) y agregar un mensaje en el código, como:
    ```python
    print("¡Hola desde la web de GitHub!")
    ```
2. Confirmar los cambios (commit) en la web.
3. Tocá el botón **Pull** en Visual Studio Code para traer todos los cambios realizados.
4. Verificá que los archivos nuevos y las modificaciones aparezcan en tu proyecto local.


---

## ✅ ¡Listo!

Ahora sabés cómo:

* Crear una cuenta en GitHub
* Trabajar con repositorios locales desde Visual Studio Code
* Subir y bajar cambios desde GitHub usando VSC
* Usar herramientas gráficas para trabajar en equipo

