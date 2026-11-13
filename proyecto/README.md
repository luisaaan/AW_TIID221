# Banco de Sangre UPQ - Flask

## Requisitos
- Python 3.10+
- MySQL / XAMPP

## Instalación
1. Ejecuta el SQL de creación de la base de datos `BancoSangre` en phpMyAdmin.
2. Abre una terminal en esta carpeta.
3. Instala dependencias: `pip install -r requirements.txt`
4. Revisa host, usuario, contraseña y puerto en `app.py`.
5. Ejecuta: `python app.py`
6. Abre `http://127.0.0.1:5000`

Las interfaces están separadas por archivo HTML dentro de `templates`; el CSS común está en `static/estilos.css`. DaisyUI se carga desde CDN.

Nota: las pantallas de administración actualmente muestran datos de ejemplo; se pueden conectar después a operaciones CRUD reales. El registro de donantes y el inicio de sesión sí tienen una conexión básica a MySQL. En un sistema real, usa hashing de contraseñas y controles de privacidad.
