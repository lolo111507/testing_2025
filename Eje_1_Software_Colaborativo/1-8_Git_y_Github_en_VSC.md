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
* Abrí la terminal (`Ctrl + ~`) y escribí:

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
git branch -M main
git push -u origin main
```

---

## 🔄 Parte 4 – Subir y bajar cambios desde Visual Studio Code

### Subir cambios (Push)

1. Hacé tus modificaciones.
2. Guardá y hacé commit.
3. Tocá el botón **Push** o el icono de sincronizar 🔃.

### Bajar cambios (Pull)

1. Si otro compañero subió algo o lo hiciste desde la web:
2. Usá el botón **Pull** para traer los cambios.

---

## ✅ ¡Listo!

Ahora sabés cómo:

* Crear una cuenta en GitHub
* Trabajar con repositorios locales desde Visual Studio Code
* Subir y bajar cambios desde GitHub usando VSC
* Usar herramientas gráficas para trabajar en equipo

