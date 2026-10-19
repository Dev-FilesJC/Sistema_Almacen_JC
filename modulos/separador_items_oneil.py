# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import re
import hashlib
from io import BytesIO
import pandas as pd
import streamlit as st

st.subheader("📦 SEPARADOR DE ITEMS ONEIL")
st.caption("Separa los códigos en filas individuales y permite compararlos con otro Excel.")

st.markdown("""
<style>
div[data-testid="stDownloadButton"] button,
div[data-testid="stButton"] button {
    min-height: 34px !important; height: auto !important;
    padding: 0.35rem 0.75rem !important; font-size: 0.88rem !important;
    white-space: normal !important;
}
</style>
""", unsafe_allow_html=True)

def separar_codigos(valor):
    if valor is None:
        return []
    texto = str(valor).strip()
    if not texto:
        return []
    return [parte.strip() for parte in re.split(r"[,;\n\r]+", texto) if parte.strip()]

def normalizar_codigo(valor):
    if valor is None:
        return ""
    return re.sub(r"\s+", "", str(valor)).strip().upper()

def crear_excel(dataframe, sheet_name="Items separados"):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(writer, index=False, sheet_name=sheet_name)
        ws = writer.sheets[sheet_name]
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                if cell.value is not None:
                    cell.number_format = "@"
        for column_cells in ws.columns:
            letter = column_cells[0].column_letter
            max_len = max((len(str(cell.value)) if cell.value is not None else 0)
                          for cell in column_cells)
            ws.column_dimensions[letter].width = min(max(max_len + 2, 12), 45)
    output.seek(0)
    return output.getvalue()

def leer_excel(upload):
    upload.seek(0)
    frame = pd.read_excel(upload, dtype=str, keep_default_na=False)
    frame.columns = [str(col).strip() for col in frame.columns]
    return frame

uploaded_file = st.file_uploader(
    "Selecciona el archivo Excel que contiene los Items Oneil",
    type=["xlsx", "xls"], key="separador_items_archivo",
    help="Puedes seleccionar otro archivo cuando quieras procesar datos nuevos."
)

if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.getvalue()
        source_id = hashlib.sha256(file_bytes).hexdigest()
        # Evita que un resultado anterior aparezca al cargar un archivo diferente,
        # incluso si ambos archivos tienen exactamente el mismo nombre.
        if st.session_state.get("items_source_id") != source_id:
            for key in ("resultado_items", "sin_codigo_items", "nombre_col_items",
                        "items_col_items", "items_archivo_origen", "items_result_source_id",
                        "resultado_comparacion", "comparacion_source_id"):
                st.session_state.pop(key, None)
            st.session_state["items_source_id"] = source_id

        df = leer_excel(uploaded_file)
        st.success(f"Archivo cargado: {uploaded_file.name}")
        st.caption(f"Filas originales: {len(df):,} · Columnas: {len(df.columns)}")

        if df.empty:
            st.warning("El archivo no contiene filas de datos.")
        else:
            with st.expander("👁️ Vista previa del archivo original", expanded=False):
                st.dataframe(df.head(10), use_container_width=True, hide_index=True)

            cols = df.columns.tolist()
            c1, c2 = st.columns(2)
            with c1:
                default_name = cols.index("Nombre") if "Nombre" in cols else 0
                nombre_col = st.selectbox(
                    "Columna que identifica la solicitud", cols,
                    index=default_name, key="items_nombre_col"
                )
            with c2:
                default_items = cols.index("Items Oneil") if "Items Oneil" in cols else min(1, len(cols) - 1)
                items_col = st.selectbox(
                    "Columna que contiene los códigos", cols,
                    index=default_items, key="items_codigo_col"
                )

            if nombre_col == items_col:
                st.error("Selecciona columnas diferentes para la solicitud y los códigos.")
            else:
                _, btn_col, _ = st.columns([1, 1.2, 1])
                with btn_col:
                    separar = st.button("✂️ Separar códigos", type="primary", key="btn_separar_items")
                if separar:
                    filas, sin_codigo = [], 0
                    for _, row in df.iterrows():
                        codigos = separar_codigos(row[items_col])
                        if not codigos:
                            sin_codigo += 1
                            continue
                        for codigo in codigos:
                            nueva_fila = row.to_dict()
                            nueva_fila[nombre_col] = str(row[nombre_col]).strip()
                            nueva_fila[items_col] = codigo
                            filas.append(nueva_fila)
                    st.session_state["resultado_items"] = pd.DataFrame(filas, columns=df.columns)
                    st.session_state["sin_codigo_items"] = sin_codigo
                    st.session_state["nombre_col_items"] = nombre_col
                    st.session_state["items_col_items"] = items_col
                    st.session_state["items_archivo_origen"] = uploaded_file.name
                    st.session_state["items_result_source_id"] = source_id
                    st.session_state.pop("resultado_comparacion", None)
                    st.session_state.pop("comparacion_source_id", None)

            if (st.session_state.get("items_result_source_id") == source_id
                    and "resultado_items" in st.session_state):
                resultado = st.session_state["resultado_items"]
                nombre_resultado = st.session_state["nombre_col_items"]
                items_resultado = st.session_state["items_col_items"]
                sin_codigo = st.session_state["sin_codigo_items"]
                st.divider()
                st.markdown("### 📋 Resultado de la separación")
                m1, m2, m3 = st.columns(3)
                m1.metric("Filas originales", f"{len(df):,}")
                m2.metric("Códigos separados", f"{len(resultado):,}")
                m3.metric("Filas sin código", f"{sin_codigo:,}")

                if resultado.empty:
                    st.warning("No se encontraron códigos para separar.")
                else:
                    st.dataframe(resultado, use_container_width=True, hide_index=True)
                    reducido = resultado[[nombre_resultado, items_resultado]].copy()
                    if nombre_resultado != "Nombre" or items_resultado != "Items Oneil":
                        reducido.columns = ["Nombre", "Items Oneil"]

                    b1, b2 = st.columns(2)
                    with b1:
                        st.download_button(
                            "📥 Descargar Excel completo",
                            data=crear_excel(resultado, "Items separados"),
                            file_name="LASERFICHE_ITEMS_SEPARADOS_COMPLETO.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key="descargar_items_completo",
                        )
                    with b2:
                        st.download_button(
                            "📥 Descargar Nombre e Items Oneil",
                            data=crear_excel(reducido, "Nombre e Items"),
                            file_name="LASERFICHE_SOLO_NOMBRE_ITEMS.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key="descargar_items_reducido",
                        )

                    st.divider()
                    st.markdown("### 🔎 Comparar con otro archivo Excel")
                    st.write(
                        "Carga el segundo Excel. Se comparará la columna **Items Oneil** "
                        "del resultado separado con la columna **Codigo del Item** del nuevo archivo. "
                        "La comparación ignora espacios y diferencias entre mayúsculas/minúsculas."
                    )
                    compare_file = st.file_uploader(
                        "Selecciona el segundo archivo Excel para comparar",
                        type=["xlsx", "xls"], key="comparar_items_archivo"
                    )
                    if compare_file is not None:
                        compare_bytes = compare_file.getvalue()
                        compare_id = hashlib.sha256(compare_bytes).hexdigest()
                        try:
                            df_compare = leer_excel(compare_file)
                            if "Codigo del Item" not in df_compare.columns:
                                st.error("El segundo archivo no contiene una columna llamada exactamente 'Codigo del Item'.")
                            else:
                                if st.button("⚖️ Comparar códigos", type="primary", key="btn_comparar_items"):
                                    codigos_referencia = {
                                        normalizar_codigo(x) for x in df_compare["Codigo del Item"].tolist()
                                        if normalizar_codigo(x)
                                    }
                                    comp = resultado.copy()
                                    comp["Estado comparación"] = comp[items_resultado].map(
                                        lambda x: "ENCONTRADO" if normalizar_codigo(x) in codigos_referencia
                                        else "NO ENCONTRADO"
                                    )
                                    st.session_state["resultado_comparacion"] = comp
                                    st.session_state["comparacion_source_id"] = source_id + ":" + compare_id

                                comparison_key = source_id + ":" + compare_id
                                if (st.session_state.get("comparacion_source_id") == comparison_key
                                        and "resultado_comparacion" in st.session_state):
                                    comp = st.session_state["resultado_comparacion"]
                                    encontrados = int((comp["Estado comparación"] == "ENCONTRADO").sum())
                                    no_encontrados = int((comp["Estado comparación"] == "NO ENCONTRADO").sum())
                                    st.markdown("#### 📊 Resultado de la comparación")
                                    m1, m2, m3 = st.columns(3)
                                    m1.metric("Códigos comparados", f"{len(comp):,}")
                                    m2.metric("Encontrados", f"{encontrados:,}")
                                    m3.metric("No encontrados", f"{no_encontrados:,}")
                                    filtro = st.radio(
                                        "Mostrar resultados", ["Todos", "Solo encontrados", "Solo no encontrados"],
                                        horizontal=True, key="filtro_resultado_comparacion"
                                    )
                                    mostrar = comp
                                    if filtro == "Solo encontrados":
                                        mostrar = comp[comp["Estado comparación"] == "ENCONTRADO"]
                                    elif filtro == "Solo no encontrados":
                                        mostrar = comp[comp["Estado comparación"] == "NO ENCONTRADO"]
                                    st.dataframe(mostrar, use_container_width=True, hide_index=True)
                                    st.download_button(
                                        "📥 Descargar resultado de comparación",
                                        data=crear_excel(comp, "Comparacion"),
                                        file_name="COMPARACION_ITEMS_ONEIL.xlsx",
                                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                        key="descargar_comparacion_items",
                                    )
                        except Exception as error:
                            st.error(f"No se pudo leer el archivo de comparación: {error}")

                    st.caption(
                        "El archivo original no se modifica. Los códigos se procesan como texto "
                        "para conservar los ceros iniciales que estén presentes en el archivo."
                    )
    except Exception as error:
        st.error(f"No se pudo leer o procesar el archivo: {error}")
else:
    # Limpia resultados anteriores cuando se retira el archivo del cargador.
    for key in ("resultado_items", "sin_codigo_items", "nombre_col_items",
                "items_col_items", "items_archivo_origen", "items_result_source_id",
                "resultado_comparacion", "comparacion_source_id", "items_source_id"):
        st.session_state.pop(key, None)
    st.info("Carga el Excel, selecciona las columnas y pulsa **Separar códigos**.")
