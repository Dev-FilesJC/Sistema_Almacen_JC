# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.subheader("🔍 CHECK FILEWEB AND LASERFICHE")

# --------------------- SIDEBAR MENU ---------------------
st.sidebar.title("Menú de Opciones")
menu = st.sidebar.radio("Ir a:", [
    "🔎 Generar Sintaxis Solicitudes",
    "🏷️ Reemplazar archivo",
    "🧩 Comparación de Solicitudes FileWeb vs LaserFiche",
    "🔎 Generar Sintaxis LaserFiche del filtrado",
    "🔎 Sintaxis ONEIL del filtrado",
    "🗑️ Eliminar Archivos Generados"

])
        
# --------------------- 1. GENERADOR DE SINTAXIS ---------------------
def Generar_Sintaxis_Solicitudes():

    st.title("🔎 GENERADOR DE SINTAXIS DE BÚSQUEDA LASER FICHE")

    if "sintaxi_final" not in st.session_state:
        st.session_state.sintaxis_final = ""
        st.session_state.sistaxis_preview = ""
        st.session_state.total_registros = 0

    col1, col2 = st.columns((2))
    with col1:
        # Cargar archivo Excel
        st.markdown("<h4>Selecciona el archivo Excel con la columna 'SolicitudCodeFileWeb'</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Selecciona un archivo .xlsx", type="xlsx")


        # Generar la sintaxis de búsqueda
        if st.button("Generar Sintaxis"):

            if uploaded_file is not None:
                try:
                    # Leer el archivo Excel y obtener solo la columna 'SolicitudCode'
                    df = pd.read_excel(uploaded_file)

                    # Verificar si la columna existe
                    if 'SolicitudCodeFileWeb' not in df.columns:
                        st.error("La columna 'SolicitudCodeFileWeb' no se encuentra en el archivo.")
                    else:
                        # Eliminar las demás columnas y eliminar nulos
                        solicitud_codes = df['SolicitudCodeFileWeb'].dropna().astype(str).tolist()

                        # Crear la sintaxis
                        #solicitud_sintaxis = " | ".join(
                            #[f'\n{{[Orden de Trabajo]:[Nro Solicitud]="{code.strip()}"}}' for code in solicitud_codes if code.strip()]
                                
                        #)
                        # 🔹 Sintaxis completa
                        sintaxis_list = [
                            f'{{[Orden de Trabajo]:[Nro Solicitud]="{code.strip()}"}}'
                            for code in solicitud_codes if code.strip()
                        ]

                        st.session_state.sintaxis_final = " | \n".join(sintaxis_list)

                        # 🔹 Preview: primeros 20
                        st.session_state.sintaxis_preview = " | \n".join(sintaxis_list[:20])
                            
                        st.session_state.total_registros = len(sintaxis_list)

                        st.success("Sintaxis generada correctamente")


                except Exception as e:
                    st.error(f"Error al leer el archivo: {e}")

        # Pie de página
        st.markdown("---")
        st.caption("ℹ️ PARA DESCARGAR DE LASER FICHE DEL CAMPO (Orden de Trabajo) AGREGAR [Nro de Solicitus y Nro de WO] ")

    with col2:
        # Mostrar la sintaxis generada
        if st.session_state.sintaxis_final:
            # 🔹 Mostrar total
            st.info(f"📊 Total de registros generados: **{st.session_state.total_registros}**")

            st.success("Sintaxis de búsqueda generada:")
            st.code(st.session_state.sintaxis_preview)

            # Boton de descarga 
            st.download_button(
                label="⬇️ Descargar Sintaxis",
                data=st.session_state.sintaxis_final,
                file_name="Sintaxis_LaserFiche.txt",
                mime="text/plain"
            )


# --------------------- 2. Reemplazar Archivos ---------------------

def Reemplazar_Archivo():
    import streamlit as st
    import pandas as pd
    import os
    import io

    #st.set_page_config(page_title="Reemplazo de Archivos Excel", page_icon="📊", layout="wide")
    st.title("Reemplazo de Archivos Excel 🗂️")

    # Función para cargar los archivos Excel
    def cargar_archivo(nombre):
        """Cargar un archivo Excel en un DataFrame y devolver el nombre del archivo."""
        archivo = st.file_uploader(f"Sube el archivo {nombre}", type=["xlsx", "xls"])
        if archivo is not None:
            # Obtener el nombre del archivo
            nombre_archivo = archivo.name
            # Cargar el archivo Excel en un DataFrame de Pandas
            df = pd.read_excel(archivo, engine='openpyxl')
            return df, nombre_archivo
        return None, None

    # Función para reemplazar los datos
    def reemplazar_datos(df1, df2):
        """Reemplazar solo los datos del archivo 1 con los datos del archivo 2, manteniendo el encabezado."""
        # Guardar el encabezado del archivo 1
        encabezado_df1 = df1.columns
            
        # Reemplazar los datos, manteniendo el encabezado del archivo 1
        df2.columns = encabezado_df1  # Aseguramos que los encabezados de df2 coincidan con df1
        df2 = df2[encabezado_df1]     # Solo tomamos las columnas de df2 que están en df1
        return df2

    # Función para guardar el archivo reemplazado en la ruta proporcionada
    def guardar_archivo(df, ruta, nombre_archivo):
        """Guardar el archivo reemplazado en la ruta especificada por el usuario."""
        if not os.path.exists(ruta):
            st.error("🚨 ¡La ruta no existe! Por favor, ingresa una ruta válida.")
            return None
            
        # Guardar el archivo como Excel en la ruta proporcionada
        ruta_completa = os.path.join(ruta, nombre_archivo)
        df.to_excel(ruta_completa, index=False, engine='openpyxl')
            
        return ruta_completa

    # Subir los dos archivos Excel
    col1, col2 = st.columns(2)
    with col1:
        archivo_1_df, nombre_archivo_1 = cargar_archivo("1")
    with col2:
        archivo_2_df, _ = cargar_archivo("2")


    # Si los archivos han sido subidos
    if archivo_1_df is not None and archivo_2_df is not None:
        # Reemplazar los datos del archivo 1 con los del archivo 2, manteniendo el encabezado de archivo 1
        archivo_reemplazado = reemplazar_datos(archivo_1_df, archivo_2_df)
            
        # Mostrar los primeros 5 registros del archivo reemplazado
        st.subheader("Archivo Reemplazado (Vista Previa) 👀")
        st.write(archivo_reemplazado.head())
            
        # Crear archivo Excel en memoria
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            archivo_reemplazado.to_excel(writer, index=False)
        buffer.seek(0)

        # Botón de descarga
        st.download_button(
            label="📥 Descargar archivo Excel",
            data=buffer,
            file_name=nombre_archivo_1,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# --------------------- 3. Comparación de Solicitudes FileWeb vs LaserFiche ---------------------
def Comparar_Solicitudes_FW_y_LF():
    import pandas as pd
    import streamlit as st
    from io import BytesIO
    from openpyxl import load_workbook
    from openpyxl.styles import PatternFill, Border, Side, Font, Alignment
    from collections import defaultdict
    import os

    st.title("📋 Comparación de Solicitudes FileWeb vs LaserFiche")

    def procesar_archivos(file1, file2):
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        # NORMALIZAR COLUMNAS (CLAVE)
        df1.columns = (
            df1.columns
            .str.replace('\n', ' ', regex=True)
            .str.replace('\xa0', ' ', regex=True)
            .str.strip()
        )

        df2.columns = (
            df2.columns
            .str.replace('\n', ' ', regex=True)
            .str.replace('\xa0', ' ', regex=True)
            .str.strip()
        )

        #st.write("Columnas LaserFiche detectadas:", list(df2.columns))

        # Asegurar que las columnas relevantes sean texto
        columnas_texto = [
            'SolicitudCodeFileWeb', 'Tipo de Solicitud FileWeb', 'Estado de Solicitud FileWeb',
            'WorkOrderCodeFileWe', 'CantidadFileWeb', 'TipoFileFileWeb', 'Centro de Costo FileWeb',
            'Fecha de Registro FileWeb', 'NombreLaserFiche', 'Cliente LaserFiche',
            'Estado de OT LaserFiche', 'Nro Solicitud laserFiche', 'Direccion'
        ]
        for df in [df1, df2]:
            for col in columnas_texto:
                if col in df.columns:
                    df[col] = df[col].astype(str).fillna("")

        merged_df = pd.merge(
            df1[['SolicitudCodeFileWeb', 'Tipo de Solicitud FileWeb', 'Estado de Solicitud FileWeb',
                'WorkOrderCodeFileWe', 'CantidadFileWeb', 'TipoFileFileWeb', 'Centro de Costo FileWeb',
                'Fecha de Registro FileWeb']],
            df2[['NombreLaserFiche', 'Cliente LaserFiche', 'Estado de OT LaserFiche', 'Nro Solicitud laserFiche', 'Direccion']],
            left_on='SolicitudCodeFileWeb',
            right_on='Nro Solicitud laserFiche',
            how='inner'
        )

        column_order = [
            'SolicitudCodeFileWeb',
            'Nro Solicitud laserFiche',
            'Tipo de Solicitud FileWeb',
            'NombreLaserFiche',
            'Estado de Solicitud FileWeb',
            'Estado de OT LaserFiche',
            'WorkOrderCodeFileWe',
            'Fecha de Registro FileWeb',
            'CantidadFileWeb',
            'TipoFileFileWeb',
            'Centro de Costo FileWeb',
            'Cliente LaserFiche',
            'Direccion'
        ]

        return merged_df[column_order]

    # Subida de archivos
    col1, col2 = st.columns(2)
    file1 = col1.file_uploader("📂 Sube archivo FileWeb", type=["xlsx"])
    file2 = col2.file_uploader("📂 Sube archivo LaserFiche", type=["xlsx"])

    if file1 and file2:
        try:
            resultado = procesar_archivos(file1, file2)

            # Comparar estados de forma segura
            resultado['Rojo'] = resultado.apply(
                lambda row: str(row['Estado de Solicitud FileWeb']).strip() != str(row['Estado de OT LaserFiche']).strip(),
                axis=1
            )

            # Opción de mostrar todo o solo diferentes
            opcion = st.radio("¿Qué archivo deseas ver y descargar?", ("Todo", "Solo Rojo"))

            if opcion == "Solo Rojo":
                resultado = resultado[resultado['Rojo'] == True]

            # Filtros
            estados_ot = sorted(resultado['Estado de OT LaserFiche'].dropna().unique())
            estado_ot = st.selectbox("📌 Filtrar por Estado de OT LaserFiche:", ["(Todos)"] + estados_ot)

            estados_fileweb = sorted(resultado['Estado de Solicitud FileWeb'].dropna().unique())
            estado_fileweb = st.selectbox("📍 Filtrar por Estado de Solicitud FileWeb:", ["(Todos)"] + estados_fileweb)

            prefijo = st.text_input("🔤 Buscar por prefijo de NombreLaserFiche (ej: OTEV, OTPM):").strip().upper()

            # Aplicar filtros
            if estado_ot != "(Todos)":
                resultado = resultado[resultado['Estado de OT LaserFiche'] == estado_ot]

            if estado_fileweb != "(Todos)":
                resultado = resultado[resultado['Estado de Solicitud FileWeb'] == estado_fileweb]

            if prefijo:
                resultado = resultado[resultado['NombreLaserFiche'].str.upper().str.startswith(prefijo)]

            st.success(f"✅ Se encontraron {len(resultado)} registros filtrados")
            st.dataframe(resultado.drop(columns=['Rojo']), height=600, use_container_width=True)

            # Exportar a Excel con formato
            resultado_exportar = resultado.drop(columns=['Rojo'])
            excel_buffer = BytesIO()
            resultado_exportar.to_excel(excel_buffer, index=False)
            excel_buffer.seek(0)

            wb = load_workbook(excel_buffer)
            ws = wb.active
            ws.auto_filter.ref = ws.dimensions

            # Estilos
            thin_border = Border(left=Side(style='thin'), right=Side(style='thin'),
                                top=Side(style='thin'), bottom=Side(style='thin'))
            header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
            header_font = Font(color="FFFFFF", bold=True)
            center_align = Alignment(horizontal="center", vertical="center")

            for cell in ws[1]:
                cell.fill = header_fill
                cell.font = header_font
                cell.alignment = center_align
                cell.border = thin_border

            # Mapeo columnas
            header_map = {str(cell.value).strip(): idx for idx, cell in enumerate(ws[1], 1)}
            col_estado1 = header_map.get("Estado de Solicitud FileWeb")
            col_estado2 = header_map.get("Estado de OT LaserFiche")
            col_workorder = header_map.get("WorkOrderCodeFileWe")

            verde = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
            rojo = PatternFill(start_color="F08080", end_color="F08080", fill_type="solid")
            intercalados = [PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid"),
                            PatternFill(start_color="FFE699", end_color="FFE699", fill_type="solid")]

            # Colorear diferencias
            for row in range(2, ws.max_row + 1):
                val1 = ws.cell(row=row, column=col_estado1).value
                val2 = ws.cell(row=row, column=col_estado2).value
                if val1 and val2:
                    if str(val1).strip() != str(val2).strip():
                        ws.cell(row=row, column=col_estado1).fill = rojo
                        ws.cell(row=row, column=col_estado2).fill = rojo
                    else:
                        ws.cell(row=row, column=col_estado1).fill = verde
                        ws.cell(row=row, column=col_estado2).fill = verde

            # Resaltar duplicados
            if col_workorder:
                duplicados = defaultdict(list)
                for row in range(2, ws.max_row + 1):
                    val = ws.cell(row=row, column=col_workorder).value
                    if val:
                        duplicados[str(val).strip()].append(row)
                grupos = [v for v in duplicados.values() if len(v) > 1]
                for i, filas in enumerate(grupos):
                    fill = intercalados[i % 2]
                    for row in filas:
                        for col in range(1, ws.max_column + 1):
                            ws.cell(row=row, column=col).fill = fill

            # Ajustar ancho y aplicar bordes
            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter
                for cell in col:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                    cell.border = thin_border
                ws.column_dimensions[col_letter].width = max_length + 2

            final_buffer = BytesIO()
            wb.save(final_buffer)
            final_buffer.seek(0)

            # Guardar localmente si se indica
            ruta_personalizada = st.text_input("📁 Ingrese una ruta de servidor para guardar el archivo (opcional):")
            if ruta_personalizada:
                try:
                    output_path = os.path.join(ruta_personalizada, "comparacion_de_solicitudes.xlsx")
                    with open(output_path, "wb") as f:
                        f.write(final_buffer.getbuffer())
                    st.success(f"✅ Archivo guardado en: {output_path}")
                except Exception as e:
                    st.error(f"❌ No se pudo guardar el archivo: {str(e)}")

            st.download_button(
                label="💾 Descargar archivo con formato",
                data=final_buffer,
                file_name="comparacion_de_solicitudes.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

    st.markdown("---")
    st.caption("🔎 Este archivo contiene filtros, bordes, colores para diferencias y filas duplicadas.")


def Generar_Sintaxis_del_filtrado():

    st.title("🔎 GENERADOR DE SINTAXIS PARA LASER FICHE DEL ARCHIVO FILTRADO")

    colum1, colum2 = st.columns((2))
    with colum1:
        # Cargar archivo Excel
        st.markdown("<h4>Selecciona el archivo Excel con la columna 'SolicitudCodeFileWeb'</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Selecciona un archivo .xlsx", type="xlsx")

        # Variable para almacenar la sintaxis generada
        sintaxis_final = ""

        # Generar la sintaxis de búsqueda
        if st.button("Generar Sintaxis"):

            if uploaded_file is not None:
                try:
                    # Leer el archivo Excel y obtener solo la columna 'SolicitudCode'
                    df = pd.read_excel(uploaded_file)

                    # Verificar si la columna existe
                    if 'SolicitudCodeFileWeb' not in df.columns:
                        st.error("La columna 'SolicitudCodeFileWeb' no se encuentra en el archivo.")
                    else:
                        # Eliminar las demás columnas y eliminar nulos
                        solicitud_codes = df['SolicitudCodeFileWeb'].dropna().astype(str).tolist()

                        # Crear la sintaxis
                        solicitud_sintaxis = " | ".join(
                            [f'\n{{[Orden de Trabajo]:[Nro Solicitud]="{code.strip()}"}}' for code in solicitud_codes if code.strip()]
                                
                        )

                        sintaxis_final = f"{solicitud_sintaxis}"
                except Exception as e:
                    st.error(f"Error al leer el archivo: {e}")

    with colum2:
        # Mostrar la sintaxis generada
        if sintaxis_final:
            st.success("Sintaxis de búsqueda generada:")
            st.code(sintaxis_final)
        
    # Pie de página
    st.markdown("---")

def Generar_Sintaxis_ONEIL_del_filtrado():
    import streamlit as st
    import pandas as pd

    st.title("🔎 GENERADOR DE SINTAXIS PARA ONEIL DEL ARCHIVO FILTRADO")
    colums1, colums2 = st.columns((2))

    with colums1:
        # Cargar archivo Excel
        st.markdown("<h4>Selecciona el archivo Excel con la columna 'SolicitudCodeFileWeb'</h4>", unsafe_allow_html=True)
        uploaded_files = st.file_uploader("Selecciona un archivo .xlsx", type="xlsx")

        # Variable para almacenar la sintaxis generada
        sintaxis_final = ""

        if st.button("Generar Sintaxis"):
            if uploaded_files is not None:
                # Leer el archivo Excel con pandas
                try:
                    df = pd.read_excel(uploaded_files)

                    # Verificar si la columna existe
                    if "SolicitudCodeFileWeb" in df.columns:
                        # Eliminar valores vacíos y construir la sintaxis
                        solicitud_numbers = df["SolicitudCodeFileWeb"].dropna().astype(str)

                        solicitud_sintaxis = " OR ".join([
                            f'\n Workorder^PONumber = "{solicitud.strip()}"'
                            for solicitud in solicitud_numbers
                        ])
                        sintaxis_final = f"{solicitud_sintaxis}"
                    else:
                        st.error("❌ La columna 'SolicitudCodeFileWeb' no se encontró en el archivo.")
                except Exception as e:
                    st.error(f"❌ Error al leer el archivo: {e}")

    with colums2:
        if sintaxis_final:
            st.success("Sintaxis de búsqueda generada:")
            st.code(sintaxis_final)

    
   
# ------************************************************************************------

def eliminar_archivos_generados():
        import streamlit as st
        import os
        import glob
        import pandas as pd

        #st.set_page_config(page_title="Eliminar Excel con vista previa", layout="centered")
        st.title("🗑️ Eliminar archivos Excel con vista previa desplegable")

        folder_input = st.text_input("Introduce la ruta de la carpeta con archivos Excel:", "C:\\Users\\juan.ramos\\Desktop\\FILTRADOR_ALMACEN\\CHECK_FILEWEB_AND_LASER_FICHE")
        if st.button("🔄 Cargar archivos"):
            st.session_state.folder = folder_input
            st.session_state.selected_files = []

        # Inicializar estados
        if 'folder' not in st.session_state:
            st.session_state.folder = ""
        if 'selected_files' not in st.session_state:
            st.session_state.selected_files = []

        folder = st.session_state.folder

        def toggle_selection(f_name):
            sel = st.session_state.selected_files
            if f_name in sel:
                sel.remove(f_name)
            else:
                sel.append(f_name)

        if folder:
            if os.path.isdir(folder):
                files = glob.glob(os.path.join(folder, "*.xlsx")) + glob.glob(os.path.join(folder, "*.xls"))
                if files:
                    st.subheader("📂 Selecciona archivos:")
                    for path in files:
                        name = os.path.basename(path)
                        selected = name in st.session_state.selected_files
                        col1, col2 = st.columns([4,1])
                        with col1:
                            st.write(name)
                        with col2:
                            if st.button("✅" if selected else "☐", key=name):
                                toggle_selection(name)
                                st.rerun()

                    if st.session_state.selected_files:
                        st.subheader("👁️ Previsualizaciones desplegables")
                        for name in st.session_state.selected_files:
                            file_path = os.path.join(folder, name)
                            with st.expander(f"Ver preview: {name}", expanded=False):
                                try:
                                    df = pd.read_excel(file_path, nrows=10)
                                    st.dataframe(df)
                                except Exception as e:
                                    st.error(f"Error leyendo {name}: {e}")

                        if st.checkbox("⚠️ Confirmo que deseo eliminar los archivos seleccionados"):
                            if st.button("🗑️ Eliminar archivos"):
                                cnt = 0
                                for name in list(st.session_state.selected_files):
                                    p = os.path.join(folder, name)
                                    if os.path.exists(p):
                                        os.remove(p)
                                        cnt += 1
                                st.success(f"Se eliminaron {cnt} archivos correctamente.")
                                st.session_state.selected_files = []
                                st.session_state.folder = ""
                                st.rerun()
                    else:
                        st.info("Selecciona archivos pulsando en los botones de la derecha.")
                else:
                    st.warning("No se encontraron archivos Excel en la carpeta.")
            else:
                st.error("La ruta no es válida o no corresponde a una carpeta.")
        else:
            st.info("Introduce la ruta y pulsa 'Cargar archivos' para empezar.")


# --------------------- EJECUTAR SEGÚN MENÚ ---------------------
if menu == "🔎 Generar Sintaxis Solicitudes":
    Generar_Sintaxis_Solicitudes()
elif menu == "🧩 Comparación de Solicitudes FileWeb vs LaserFiche":
    Comparar_Solicitudes_FW_y_LF()
elif menu == "🏷️ Reemplazar archivo":
    Reemplazar_Archivo()
elif menu == "🔎 Generar Sintaxis LaserFiche del filtrado":
    Generar_Sintaxis_del_filtrado()
elif menu == "🔎 Sintaxis ONEIL del filtrado":
    Generar_Sintaxis_ONEIL_del_filtrado()
elif menu == "🗑️ Eliminar Archivos Generados":
    eliminar_archivos_generados()
