# Mapa del código — Sistema de Almacén JC

## Archivo principal
- `app.py`: imports, estilos, usuarios/permisos, inicio de sesión, menú y llamada al enrutador.
- `modulos/page_router.py`: conecta el nombre seleccionado en el menú con el archivo de pantalla.

## Pantallas
- `modulos/portada.py`: PORTADA.
- `modulos/filtrador_almacen.py`: FILTRADOR ALMACEN.
- `modulos/calendario_almacen.py`: CALENDARIO ALMACEN.
- `modulos/crear_guia_ruta.py`: CREAR GUIA RUTA LA PAZ.
- `modulos/check_fileweb_laserfiche.py`: CHECK FILEWEB AND LASERFICHE.
- `modulos/sintaxis_laserfiche_oneil.py`: SINTAXIS LASERFICHE-ONEIL.
- `modulos/duplicar_filas.py`: DUPLICAR FILAS.
- `modulos/juega_con_dino.py`: JUEGA CON DINO.
- `modulos/pagina_no_encontrada.py`: pantalla de respaldo si la opción no coincide.

## Cómo se conecta
`app.py` obtiene la opción del menú y llama `render_page(proyecto, globals())`. El enrutador carga el archivo correspondiente y lo ejecuta en el espacio compartido de `app.py`. Esta solución permite separar archivos sin cambiar de una vez todas las variables compartidas del programa original.

## Siguiente paso recomendado
Separar el código interno de las tres pantallas más grandes (Filtrador, Calendario y Crear Guía Ruta) en funciones/componentes reutilizables, verificando cada una en la aplicación de prueba.
