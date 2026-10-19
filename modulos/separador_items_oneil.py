# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import re
from io import BytesIO
import pandas as pd
import streamlit as st

st.subheader("📦 SEPARADOR DE ITEMS ONEIL")
st.caption("Separa los códigos en filas individuales y conserva los datos de cada solicitud.")

st.markdown("""
<style>
/* Estilos limitados a esta página para no alterar el resto del Sistema Almacén */
.items-wrap {max-width: 980px; margin: 0 auto;}
div[data-testid="stDownloadButton"] button,
div[data-testid="stButton"] button {
    min-height: 34px !important;
    height: auto !important;
    padding: 0.35rem 0.75rem !important;
    font-size: 0.88rem !important;
    white-space: normal !important;
}
</style>
""", unsafe_allow_html=True)

def separar_codigos(valor):
    """Divide por coma, punto y coma o salto de línea y limpia espacios."""
    if valor is None:
        return []
    texto = str(valor).strip()
    if not texto:
        return []
    return [parte.strip() for parte in re.split(r"[,;\n\r]+", texto) if parte.strip()]

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
            max_len = max(
                (len(str(cell.value)) if cell.value is not None else 0)
                for cell in column_cells
            )
            ws.column_dimensions[letter].width = min(max(max_len + 2, 12), 45)
    output.seek(0)
    return output.getvalue()

with st.container():
    uploaded_file = st.file_uploader(
        "Selecciona el archivo Excel",
        type=["xlsx", "xls"],
        help="Por ejemplo: LASERFICHE-SR2.xlsx",
        key="separador_items_archivo",
    )

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, dtype=str, keep_default_na=False)
        df.columns = [str(col).strip() for col in df.columns]
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
                    filas = []
                    sin_codigo = 0
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

            if (
                "resultado_items" in st.session_state
                and st.session_state.get("items_archivo_origen") == uploaded_file.name
            ):
                resultado = st.session_state["resultado_items"]
                nombre_resultado = st.session_state["nombre_col_items"]
                items_resultado = st.session_state["items_col_items"]
                sin_codigo = st.session_state["sin_codigo_items"]
                st.divider()
                st.markdown("### 📋 Resultado")
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

                    b1, b2, b3 = st.columns([1, 1.5, 1])
                    with b1:
                        st.download_button(
                            "📥 Excel completo",
                            data=crear_excel(resultado, "Items separados"),
                            file_name="LASERFICHE_SR2_ITEMS_SEPARADOS_COMPLETO.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key="descargar_items_completo",
                        )
                    with b2:
                        st.download_button(
                            "📥 Solo Nombre e Items Oneil",
                            data=crear_excel(reducido, "Nombre e Items"),
                            file_name="LASERFICHE_SR2_SOLO_NOMBRE_ITEMS.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key="descargar_items_reducido",
                        )
                    st.caption(
                        "El archivo original no se modifica. Los códigos se procesan como texto "
                        "para conservar los ceros iniciales que estén presentes en el archivo."
                    )
    except Exception as error:
        st.error(f"No se pudo leer o procesar el archivo: {error}")
else:
    st.info(
        "Carga el Excel, selecciona la columna de solicitud y la columna Items Oneil, "
        "y pulsa **Separar códigos**. Luego podrás descargar el resultado."
    )
