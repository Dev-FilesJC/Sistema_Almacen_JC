# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
st.subheader("📅 CALENDARIO ALMACEN")
import io
    
st.markdown("<h1 style='text-align: center;'>CALENDARIO ALMACEN LA PAZ</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'> CARGAR PLANILLA DE EXCEL PARA REALIZAR EL CALENDARIO</h2>", unsafe_allow_html=True)

#Cargar el archivo de excel 
uploaded_file = st.file_uploader('SUBE TU ARCHIVO DE EXCEL', type=['xlsx','xls'])

if uploaded_file is not None:
# Leer el archivo Excel usando Pandas
    df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Elimoinar Columnas
    Eliminar = df.drop(['ELIMINAR_1', 'ELIMINAR_2', 'ELIMINAR_3', 'ELIMINAR_4', 'ELIMINAR_5','ELIMINAR_6','ELIMINAR_7','ELIMINAR_8','ELIMINAR_9','ELIMINAR_10','ELIMINAR_11','ELIMINAR_12','ELIMINAR_13'], axis=1, errors='ignore')
    Separar = Eliminar["LOCACION"].str.split('[.-]', expand=True)
    Separar.columns = ['GALPON','LA','PASILLO','SHELF','NIVEL','COLUMNA']
    Eliminar = pd.concat([Separar, Eliminar], axis=1)
    Eliminar = Eliminar.drop(['LOCACION', 'LA'], axis=1)


    #st.dataframe(Eliminar)
    co1, co2 = st.columns(2)

    with co1:
        opciones = ["SELECCIONA UNA OPCION", "CALENDARIO GENERAL", "CALENDARIO POR PASILLO", "CALENDARIO POR SHELF"]

        seleccion = st.selectbox("Selecciona una opcion del menu: ", opciones)

    with co2:
        ruta = st.text_input("Introduce la ruta de la carpeta: ", "")

    # Función para resaltar valores mayores a 10
    def highlight_integers(values):
        if values == 0:
            return 'background-color: green'
        elif values in range(1, 12):
            return 'background-color: orange'
        elif values in range(13, 25):
            return 'background-color: red'
        return ''
        

    if seleccion == "SELECCIONA UNA OPCION":   
        pass

    elif seleccion == "CALENDARIO GENERAL":

        Calendario = Eliminar.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
            
        # Reemplazar los valores None con 0
        Calendario = Calendario.fillna(0).astype(int)

            
        #----******************************************************---
        #SACAR DATOS DEL CALENDARIO 
        # 1. TOTAL_CELDAS: filas por galpón * columnas
        total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
        total_celdas = total_celdas.rename('TOTAL_SHELS')
        # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
        nonzero_mask = (Calendario != 0)
        total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
        total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
        # 3. ESPACIOS_LIBRES: suma de ceros
        zero_mask = (Calendario == 0)
        espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
        espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
        # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
        total_cajas_para_asignar = espacios_libres * 12
        total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
        # Unir todo en un solo DataFrame
        result = pd.concat([
            total_celdas,
            total_cajas_asignadas,
            espacios_libres,
            total_cajas_para_asignar
        ], axis=1).reset_index()
                
        # Contar cendas myores a 12 
        greater_than_12 = (Calendario > 12)
        # Contar celdas mayores a 12 por NIVEL
        count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

        # Resetear índice para mejor visualización
        count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
        count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

        #---*******************************************************---

        Calendario = Calendario.style.applymap(highlight_integers)
            
        st.write(Calendario)
            
        #----*****************DESCARGAR ARCHIVO*****************************

        from xlsxwriter.utility import xl_range

        # ✅ Nombre seguro para archivo
        file_name = f"CALENDARIO_GENERAL_{pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        safe_file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-") + ".xlsx"

        # ✅ Quitar estilos de Calendario si los tiene
        calendario_clean = Calendario.data if hasattr(Calendario, 'data') else Calendario

        # ✅ Crear archivo Excel en memoria
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            workbook = writer.book

            # 🧾 HOJA: CALENDARIO COMPLETO
            sheetname = 'Calendario Completo'
            calendario_clean.to_excel(writer, sheet_name=sheetname, index=True)
            worksheet = writer.sheets[sheetname]

            # ❄️ Congelar primera fila y 3 primeras columnas
            worksheet.freeze_panes(2, 4)

            # 📐 Determinar dimensiones
            n_rows, n_cols = calendario_clean.shape
            n_index_levels = calendario_clean.index.nlevels

            start_row = 1  # headers
            start_col = n_index_levels  # después de las columnas de índice

            end_row = start_row + n_rows - 1
            end_col = start_col + n_cols - 1

            cell_range = xl_range(start_row, start_col, end_row, end_col)

            # 🎨 Formatos condicionales
            formato_verde = workbook.add_format({'bg_color': '#92D050', 'border': 1})
            formato_naranja = workbook.add_format({'bg_color': '#FFC000', 'border': 1})
            formato_rojo = workbook.add_format({'bg_color': '#FF0000', 'border': 1})

            # ✅ Condiciones de color
            worksheet.conditional_format(cell_range, {
                'type': 'cell',
                'criteria': '==',
                'value': 0,
                'format': formato_verde
            })

            worksheet.conditional_format(cell_range, {
                'type': 'cell',
                'criteria': 'between',
                'minimum': 1,
                'maximum': 11,
                'format': formato_naranja
            })

            worksheet.conditional_format(cell_range, {
                'type': 'cell',
                'criteria': '>=',
                'value': 12,
                'format': formato_rojo
            })

            # 📏 Ajuste automático de columnas
            for i, col in enumerate(calendario_clean.columns):
                header = ' '.join(map(str, col)) if isinstance(col, tuple) else str(col)
                max_len = max(len(header), 5)
                worksheet.set_column(i + n_index_levels, i + n_index_levels, max_len + 2)

            # 🔄 Ajuste de ancho para columnas de índice
            for i in range(n_index_levels):
                index_name = calendario_clean.index.names[i] or f"Index_{i}"
                worksheet.set_column(i, i, len(index_name) + 4)

            # 🧾 HOJAS ADICIONALES
            result.to_excel(writer, index=False, sheet_name='Datos por Galpón')
            count_greater_than_12_by_nivel.to_excel(writer, index=False, sheet_name='Asignaciones en Exceso')
            Eliminar.to_excel(writer, index=False, sheet_name='Base de Datos')

        # 🧷 Finalizar el archivo
        output.seek(0)

        # 📥 Botón de descarga en Streamlit
        st.download_button(
            label="📥 Descargar Excel con Formato",
            data=output.getvalue(),
            file_name=safe_file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # 💾 Guardar localmente si se da ruta
        try:
            if ruta:
                save_path = Path(ruta) / safe_file_name
                with open(save_path, 'wb') as f:
                    f.write(output.getvalue())
                st.success(f"✅ Archivo guardado localmente en: {save_path.resolve()}")
        except Exception as e:
            st.warning(f"⚠️ No se pudo guardar localmente. Error: {str(e)}")

            
        # Mostrar en Streamlit

        colum1, colum2 = st.columns([12.04, 14.04])

        with colum1:
            #st.write("ASIGNACIONES QUE SOBREPASAN SU CANTIDAD LIMITE")
            st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)  
            st.table(count_greater_than_12_by_nivel)

        with colum2:
            #st.write("DATOS POR GAPON:")
            st.markdown("<h3 style='text-align: center;'>DATOS POR GAPON</h3>", unsafe_allow_html=True) 
            st.table(result)

        #---*******************************************************---

        #---*******************************************************---
        #  FILTRAR CODIGOS DE UN SHELF INDICADO
        #---*******************************************************---
        st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

        # Crear un selector para elegir una celda
        galpones = Calendario.index.get_level_values('GALPON').unique()
        pasillos = Calendario.index.get_level_values('PASILLO').unique()
        niveles = Calendario.index.get_level_values('NIVEL').unique()
        shelfs = Calendario.columns.levels[0].tolist()
        columnas = Calendario.columns.levels[1].tolist()
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
        with col2:
            selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
        with col3:
            selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
        with col4:
            selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
        with col5:
            selected_columna = st.selectbox("Selecciona una Columna:", columnas)
        # Filtrar los códigos poly según la selección
        if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
            filtered_data = Eliminar[
                (Eliminar['GALPON'] == selected_galpon) &
                (Eliminar['PASILLO'] == selected_pasillo) &
                (Eliminar['NIVEL'] == selected_nivel) &
                (Eliminar['SHELF'] == selected_shelf) &
                (Eliminar['COLUMNA'] == selected_columna)
            ]

            # Asegurarse de que solo se muestren las columnas deseadas
            columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
            filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

            # Renumerar los registros comensando desde 1
            filtered_data.index = filtered_data.index +1

            # Mostrar los códigos poly en una tabla
            st.write("Códigos Poly asignados a la celda seleccionada:")
            st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

        #---********************************************************---

    elif seleccion == "CALENDARIO POR PASILLO":

        file_name = st.selectbox("Guardar Como:", options = ["OPCIONES","PASILLO_A", "PASILLO_B", "PASILLO_C", "PASILLO_D", "PASILLO_E", "PASILLO_F", "PASILLO_G", "PASILLO_H", "PASILLO_I"])
                        
        Pasillo = st.selectbox("Buscar Pasillo", options = ["PASILLO", "A", "B", "C", "D", "E", "F", "G", "H", "I"])

        if Pasillo == "PASILLO":
            pass

        if Pasillo == "A":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_A" and Pasillo == "A":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.write("DATOS POR GAPON:")
                st.table(result)

            #---*******************************************************---              

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---
    
        if Pasillo == "B":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)

            #---********************************************************---
    
            if file_name == "PASILLO_B" and Pasillo == "B":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True) 
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.write("DATOS POR GAPON:")
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

        #---*******************************************************************---            

        if Pasillo == "C":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')

            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)


            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---


            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_C" and Pasillo == "C":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---

        if Pasillo == "D":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_D" and Pasillo == "D":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---

        if Pasillo == "E":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---


            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_E" and Pasillo == "E":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True) 
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATO POR GALPON</h3>", unsafe_allow_html=True) 
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---

        if Pasillo == "F":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)

                
            if file_name == "PASILLO_F" and Pasillo == "F":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True) 
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---


        if Pasillo == "G":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_G" and Pasillo == "G":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---

            
        if Pasillo == "H":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---


            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)

                
            if file_name == "PASILLO_H" and Pasillo == "H":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---

        if Pasillo == "I":

            Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

            Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')
        
            # Reemplazar los valores None con 0
            Calendario = Calendario.fillna(0).astype(int)

            #----******************************************************---
            #SACAR DATOS DEL CALENDARIO 
            # 1. TOTAL_CELDAS: filas por galpón * columnas
            total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
            total_celdas = total_celdas.rename('TOTAL_SHELS')
            # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
            nonzero_mask = (Calendario != 0)
            total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
            total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
            # 3. ESPACIOS_LIBRES: suma de ceros
            zero_mask = (Calendario == 0)
            espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
            espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
            # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
            total_cajas_para_asignar = espacios_libres * 12
            total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
            # Unir todo en un solo DataFrame
            result = pd.concat([
                total_celdas,
                total_cajas_asignadas,
                espacios_libres,
                total_cajas_para_asignar
            ], axis=1).reset_index()
                
            # Contar cendas myores a 12 
            greater_than_12 = (Calendario > 12)
            # Contar celdas mayores a 12 por NIVEL
            count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

            # Resetear índice para mejor visualización
            count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
            count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

            #---*******************************************************---

            Calendario = Calendario.style.applymap(highlight_integers)

            st.write(Calendario)


            if file_name == "PASILLO_I" and Pasillo == "I":
                    
                file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                # Definir la ruta de guardado
                save_dir = Path(ruta)  # Directorio donde se guardarán los archivos

                #save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                # Guardar el DataFrame en un archivo Excel físico
                file_path =  save_dir / f"{file_name}.xlsx"

                # Guardar el dataFrame en el archivo Excel
                with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                    Calendario.to_excel(writer, index=True) # Guardar el primer dataFrame 

                # Informar al usuario donde se guardo ek archivo
                st.write(f"Archivo Guardo en: {file_path.resolve()} ")

                # Mostrar el boton de descarga para descargar el archivo guardado
                with open(file_path, "rb") as file:
                    st.download_button(
                    label="Descargar Excel",
                    data=file,
                    file_name=f"{file_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            #---********************************************************---
            # Mostrar en Streamlit
            colum1, colum2 = st.columns([12.04, 14.04])
            with colum1:
                st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True)
                st.table(count_greater_than_12_by_nivel)
            with colum2:
                st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
                st.table(result)

            #---*******************************************************---

            #---*******************************************************---
            #  FILTRAR CODIGOS DE UN SHELF INDICADO
            #---*******************************************************---
            st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

            # Crear un selector para elegir una celda
            galpones = Calendario.index.get_level_values('GALPON').unique()
            pasillos = Calendario.index.get_level_values('PASILLO').unique()
            niveles = Calendario.index.get_level_values('NIVEL').unique()
            shelfs = Calendario.columns.levels[0].tolist()
            columnas = Calendario.columns.levels[1].tolist()
                
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
            with col2:
                selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
            with col3:
                selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
            with col4:
                selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
            with col5:
                selected_columna = st.selectbox("Selecciona una Columna:", columnas)
            # Filtrar los códigos poly según la selección
            if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
                filtered_data = Eliminar[
                    (Eliminar['GALPON'] == selected_galpon) &
                    (Eliminar['PASILLO'] == selected_pasillo) &
                    (Eliminar['NIVEL'] == selected_nivel) &
                    (Eliminar['SHELF'] == selected_shelf) &
                    (Eliminar['COLUMNA'] == selected_columna)
                ]

                # Asegurarse de que solo se muestren las columnas deseadas
                columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
                filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

                # Renumerar los registros comensando desde 1
                filtered_data.index = filtered_data.index +1

                # Mostrar los códigos poly en una tabla
                st.write("Códigos Poly asignados a la celda seleccionada:")
                st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])

            #---********************************************************---


    elif seleccion == "CALENDARIO POR SHELF":

        Pasillo = st.selectbox("Buscar Pasillo", options = ["PASILLO", "A", "B", "C", "D", "E", "F"])

        Calendario = Eliminar[(Eliminar["PASILLO"] == Pasillo)]

        Shelf = st.selectbox("Buscar Shelf", options = ["TODOS","01", "02", "03", "04", "05", "06", "07", "08", "09"]) 

         
       # Shelf = st.text_input("Ingrese Numero de Shelf: ")

        Calendario = Calendario[(Calendario["SHELF"] == Shelf)]

        # Crear una tabla dinamica para mostrar el calendario

        Calendario = Calendario.pivot_table(index=["GALPON", "PASILLO", "NIVEL"], columns=["SHELF", "COLUMNA"], values=['CODIGO POLY'], aggfunc='size')

        # Reemplazar los valores None con 0
        Calendario = Calendario.fillna(0).astype(int)

        #----******************************************************---
        #SACAR DATOS DEL CALENDARIO 
        # 1. TOTAL_CELDAS: filas por galpón * columnas
        total_celdas = Calendario.groupby(level='GALPON').size() * Calendario.shape[1]
        total_celdas = total_celdas.rename('TOTAL_SHELS')
        # 2. TOTAL_CAJAS_ASIGNADAS: suma valores distintos de cero
        nonzero_mask = (Calendario != 0)
        total_cajas_asignadas = (nonzero_mask * Calendario).groupby(level='GALPON').sum().sum(axis=1)
        total_cajas_asignadas = total_cajas_asignadas.rename('TOTAL_CAJAS_ASIGNADAS')
        # 3. ESPACIOS_LIBRES: suma de ceros
        zero_mask = (Calendario == 0)
        espacios_libres = zero_mask.groupby(level='GALPON').sum().sum(axis=1)
        espacios_libres = espacios_libres.rename('ESPACIOS_LIBRES')
        # 4. TOTAL_CAJAS_PARA_ASIGNAR: multiplicacion de espacios libres por 12
        total_cajas_para_asignar = espacios_libres * 12
        total_cajas_para_asignar = total_cajas_para_asignar.rename('TOTAL_CAJAS_PARA_ASIGNAR')
        # Unir todo en un solo DataFrame
        result = pd.concat([
            total_celdas,
            total_cajas_asignadas,
            espacios_libres,
            total_cajas_para_asignar
        ], axis=1).reset_index()
                
        # Contar cendas myores a 12 
        greater_than_12 = (Calendario > 12)
        # Contar celdas mayores a 12 por NIVEL
        count_greater_than_12_by_nivel = greater_than_12.groupby(level=['GALPON','NIVEL']).sum().sum(axis=1)

        # Resetear índice para mejor visualización
        count_greater_than_12_by_nivel = count_greater_than_12_by_nivel.reset_index()
        count_greater_than_12_by_nivel.columns = ['GALPON', 'NIVEL', 'ASIGNACION EN EXCESO']

        #---*******************************************************---

        Calendario = Calendario.style.applymap(highlight_integers)

        st.write(Calendario)

        #---********************************************************---
        # Mostrar en Streamlit
        colum1, colum2 = st.columns([12.04, 14.04])
        with colum1:
            st.markdown("<h3 style='text-align: center;'>ASIGNACIONES EN EXCESO</h3>", unsafe_allow_html=True) 
            st.table(count_greater_than_12_by_nivel)
        with colum2:
            st.markdown("<h3 style='text-align: center;'>DATOS POR GALPON</h3>", unsafe_allow_html=True)
            st.table(result)

        #---*******************************************************---

        #---*******************************************************---
        #  FILTRAR CODIGOS DE UN SHELF INDICADO
        #---*******************************************************---
        st.markdown("<h3 style='text-align: center;'>MOSTRAR CAJAS DE SHEL SELECCIONADO</h3>", unsafe_allow_html=True)

        # Crear un selector para elegir una celda
        galpones = Calendario.index.get_level_values('GALPON').unique()
        pasillos = Calendario.index.get_level_values('PASILLO').unique()
        niveles = Calendario.index.get_level_values('NIVEL').unique()
        shelfs = Calendario.columns.levels[0].tolist()
        columnas = Calendario.columns.levels[1].tolist()
                
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            selected_galpon = st.selectbox("Selecciona un Galpón:", galpones)
        with col2:
            selected_pasillo = st.selectbox("Selecciona un Pasillo:", pasillos)
        with col3:
            selected_nivel = st.selectbox("Selecciona un Nivel:", niveles)
        with col4:
            selected_shelf = st.selectbox("Selecciona un Shelf:", shelfs)
        with col5:
            selected_columna = st.selectbox("Selecciona una Columna:", columnas)
        # Filtrar los códigos poly según la selección
        if selected_galpon and selected_pasillo and selected_nivel and selected_shelf and selected_columna:
            filtered_data = Eliminar[
                (Eliminar['GALPON'] == selected_galpon) &
                (Eliminar['PASILLO'] == selected_pasillo) &
                (Eliminar['NIVEL'] == selected_nivel) &
                (Eliminar['SHELF'] == selected_shelf) &
                (Eliminar['COLUMNA'] == selected_columna)
            ]

            # Asegurarse de que solo se muestren las columnas deseadas
            columns_to_show = ['GALPON', 'PASILLO', 'NIVEL','SHELF', 'COLUMNA', 'CODIGO POLY']
            filtered_data = filtered_data[columns_to_show].reset_index(drop=True)

            # Renumerar los registros comensando desde 1
            filtered_data.index = filtered_data.index +1

            # Mostrar los códigos poly en una tabla
            st.write("Códigos Poly asignados a la celda seleccionada:")
            st.dataframe(filtered_data[['GALPON', 'PASILLO', 'NIVEL', 'SHELF', 'COLUMNA', 'CODIGO POLY']])
