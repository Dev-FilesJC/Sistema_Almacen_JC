# Sistema de Almacén JC — versión compacta para Streamlit

## Organización
Esta versión mantiene el sistema en pocos archivos: `app.py` contiene el inicio de sesión, los permisos y el menú; `modulos/` contiene una pantalla por archivo y conserva las pantallas grandes completas para evitar dividir el proyecto en decenas de archivos.

## Usuarios y contraseñas en Streamlit Cloud (no en GitHub)
1. Abre el proyecto en Streamlit Community Cloud.
2. Entra a **Settings → Secrets**.
3. Copia la estructura de `SECRETS_EJEMPLO.toml` y pégala en el campo Secrets.
4. Cambia los valores `CAMBIA_ESTA_CLAVE...` por contraseñas nuevas y seguras.
5. Guarda los cambios y reinicia/reinicia la aplicación si te lo solicita.

Los usuarios, sus contraseñas y roles se leen desde `st.secrets`. No se guardan contraseñas en `app.py`. El archivo `SECRETS_EJEMPLO.toml` solo tiene marcadores de posición, no contraseñas reales.

## Subir a GitHub
- Sube el contenido de esta carpeta al repositorio; conserva la carpeta `modulos/` completa.
- En Streamlit Community Cloud selecciona `app.py` como **Main file path**.
- No subas ningún archivo llamado `secrets.toml` con credenciales reales.
- El `.gitignore` excluye `.streamlit/secrets.toml` por seguridad.

## Probar localmente
Instala dependencias con `python -m pip install -r requirements.txt` y ejecuta `streamlit run app.py`. Para probar el inicio de sesión local, configura los mismos secretos en `.streamlit/secrets.toml` (este archivo es local y no debe subirse a GitHub).

## Importante sobre seguridad
Las contraseñas de versiones anteriores estaban escritas en el código. Cámbialas por contraseñas nuevas en Streamlit Secrets, especialmente si esas versiones fueron subidas a algún repositorio.
