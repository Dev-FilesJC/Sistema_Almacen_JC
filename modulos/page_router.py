"""Enrutador de páginas del sistema de almacén.
Las páginas se ejecutan en el espacio global de app.py para conservar compatibilidad durante la separación gradual.
"""
from pathlib import Path

PAGINAS = {
    'PORTADA': 'portada',
    'FILTRADOR ALMACEN': 'filtrador_almacen',
    'CALENDARIO ALMACEN': 'calendario_almacen',
    'CREAR GUIA RUTA LA PAZ': 'crear_guia_ruta',
    'CHECK FILEWEB AND LASERFICHE': 'check_fileweb_laserfiche',
    'SINTAXIS LASERFICHE-ONEIL': 'sintaxis_laserfiche_oneil',
    'DUPLICAR FILAS': 'duplicar_filas',
    'SEPARADOR ITEMS ONEIL': 'separador_items_oneil',
    'JUEGA CON DINO': 'juega_con_dino',
}

def render_page(proyecto, namespace):
    nombre = PAGINAS.get(proyecto, "pagina_no_encontrada")
    archivo = Path(__file__).resolve().parent / f"{nombre}.py"
    codigo = archivo.read_text(encoding="utf-8")
    exec(compile(codigo, str(archivo), "exec"), namespace, namespace)
