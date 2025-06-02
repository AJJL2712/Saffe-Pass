# 🔐 SaffePass - Gestor de Contraseñas Profesional

SaffePass es una aplicación de escritorio desarrollada en Python con interfaz moderna gracias a `ttkbootstrap`. Permite gestionar contraseñas de manera segura, visual y eficiente. Ideal para quienes buscan aprender o mostrar habilidades profesionales en interfaces gráficas con Python.

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

📅 Características

* ✅ Interfaz moderna inspirada en Bitwarden
* 🔐 Almacenamiento cifrado local (Fernet/AES)
* 🎲 Generador de contraseñas seguras
* 👁️ Visor profesional en ventana modal
* 📋 Copiar contraseña al portapapeles
* 🌚 Modo claro/oscuro
* 🧹 Botón para limpiar campos
* 📄 Exportable como `.exe` con icono personalizado

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

📊 Capturas

| Interfaz Principal              | Ventana Modal (Contraseña)        |
| ------------------------------- | --------------------------------- |
| ![main](assets/screen_main.png) | ![modal](assets/screen_modal.png) |

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

⚙️ Requisitos

* Python 3.10 o superior
* Windows 10/11 (para ejecutable `.exe`)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

## 🔄 Ejecutar desde el código fuente

```bash
python src/main.py
```

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

💾 Ejecutable (.exe)

Puedes ejecutar directamente:

```
dist/SaffePass.exe
```

📥 Descargar ejecutable

[Descargar .exe desde Google Drive / GitHub Releases](https://github.com/TU_USUARIO/SaffePass/releases)

> Reemplaza este enlace por el tuyo una vez subido el `.exe`

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

👤 Autor

**Alan Jahir**
Estudiante de Ingeniería en Sistemas de Información
[LinkedIn](https://linkedin.com/in/alanjahir) | [GitHub](https://github.com/AJJL2712)

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

📄 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

📘 Recursos

* `src/gui.py` - Interfaz principal con ttkbootstrap
* `src/password_manager.py` - Lógica de almacenamiento cifrado
* `src/encryption.py` - Módulo de cifrado Fernet (clave local)
* `src/password_generator.py` - Contraseñas aleatorias seguras

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

> Proyecto realizado como ejemplo profesional de app de escritorio en Python 🚀
