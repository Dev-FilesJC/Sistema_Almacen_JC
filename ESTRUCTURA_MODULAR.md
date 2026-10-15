# Estructura compacta

- `app.py`: configuración visual, usuarios leídos desde Streamlit Secrets, permisos, login y menú principal.
- `modulos/page_router.py`: abre la pantalla elegida.
- `modulos/portada.py`: portada.
- `modulos/filtrador_almacen.py`: filtrador de almacén.
- `modulos/calendario_almacen.py`: calendario de almacén.
- `modulos/crear_guia_ruta.py`: herramientas de creación de guía de ruta, mantenidas juntas.
- `modulos/check_fileweb_laserfiche.py`: utilidades FileWeb/Laserfiche.
- `modulos/sintaxis_laserfiche_oneil.py`: generadores de sintaxis, mantenidos juntos.
- `modulos/duplicar_filas.py`: duplicación de filas.
- `modulos/juega_con_dino.py`: juego del dinosaurio.

La estructura evita separar cada botón o función en un archivo propio. Las pantallas más extensas siguen agrupadas por funcionalidad para que haya pocos archivos que mantener.
