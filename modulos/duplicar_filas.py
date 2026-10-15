# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import streamlit as st
import pandas as pd
from io import BytesIO

st.subheader("📑 DUPLICAR FILAS DE ARCHIVO EXCEL")

# Cargar archivo Excel
uploaded_file = st.file_uploader("Elige un archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Mostrar el DataFrame original
    st.write("DataFrame Original:")
    st.dataframe(df)

    # Duplicar filas
    if st.button("Duplicar Filas"):
        # Crear un nuevo DataFrame duplicando cada fila
        duplicated_rows = pd.DataFrame(columns=df.columns)
                
        for index, row in df.iterrows():
            duplicated_rows = pd.concat([duplicated_rows, pd.DataFrame([row])], ignore_index=True)
            duplicated_rows = pd.concat([duplicated_rows, pd.DataFrame([row])], ignore_index=True)

        st.write("DataFrame Duplicado:")
        st.dataframe(duplicated_rows)

        # Opción para descargar el archivo duplicado como Excel
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Duplicado')
            return output.getvalue()

        excel_data = to_excel(duplicated_rows)
        st.download_button("Descargar archivo duplicado como Excel", excel_data, "duplicado.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
