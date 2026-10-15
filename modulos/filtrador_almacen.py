# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
st.subheader("📦 FILTRADOR ALMACEN")
st.markdown("<h1 style='text-align: center;'>FILTRADO DE DOCUMENTOS Y CAJAS ALMACEN</h1>", unsafe_allow_html=True)

opciones = ["SELECCIONA UNA OPCION", "FILTRADO FILES", "FILTRADO TOMOS", "FILTRADO DE CAJAS"]

# 🔹 Creamos 3 columnas para centrar el contenido
left, center, right = st.columns([1,2,1])
   
with left:
    seleccion = st.selectbox("Selecciona una opcion del menu: ", opciones)

if seleccion == "SELECCIONA UNA OPCION":   
    st.markdown("""
    <div style="
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        background-color: #13161F;
        border: 1px solid #2d3748;
    ">
        <h1 style="color:white;">BIENVENIDO !! FILTRADO DE DOCUMENTOS ALMACEN</h1>
        <p style="color:#9ca3af;"><strong>Desarrollado por Juan Carlos Ramos Chura @2026</strong></p>
    </div>
    """, unsafe_allow_html=True)

elif seleccion == "FILTRADO FILES":

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h2 style='text-align: center;'>CARGAR PLANILLA DE EXCEL PARA FILTRAR FILES</h2>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader('Sube tu archivo de Excel', type=['xlsx','xls'])


        if uploaded_file is not None:
            
            df = pd.read_excel(uploaded_file, engine='openpyxl')

            Eliminar = df.drop(['ELIMINAR_1', 'ELIMINAR_2', 'ELIMINAR_3', 'ELIMINAR_4', 'ELIMINAR_5','ELIMINAR_6','ELIMINAR_7','ELIMINAR_8'], axis=1)
            Separar = Eliminar["LOCACION"].str.split('[.-]', expand=True)
            Separar.columns = ['G','LA','P','S','N','L']
            Eliminar = pd.concat([Separar, Eliminar], axis=1)
            Eliminar = Eliminar.drop(['LOCACION'], axis=1)
                
            ruta = st.text_input("Introduce la ruta de la carpeta para guardar los Archivos: Obligatorio", "C:\\")
        
            st.write('FILTRADO POR NIVELES:')

            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES","Nivel_1", "Nivel_2", "Nivel_3", "Nivel_4", "Nivel_5", "Nivel_6"])
                
            Nivel = st.selectbox("Buscar Nivel", options = ["NIVEL", "1", "2", "3", "4", "5", "6"])

            if file_name == " " and Nivel == " ":
                pass

            if Nivel == "1":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_1" and Nivel == "1":

                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                        
                    save_dir = Path(ruta)  # Directorio donde se guardarán los archivos


                    file_path =  save_dir / f"{file_name}.xlsx"

                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "2":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_2" and Nivel == "2":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "3":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_3" and Nivel == "3":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")


                    save_dir = Path(ruta)

                    file_path =  save_dir / f"{file_name}.xlsx"

                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


            if Nivel == "4":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_4" and Nivel == "4":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "5":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_5" and Nivel == "5":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")


                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "6":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_6" and Nivel == "6":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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
    
            # Mostrar un mensaje
            st.write('FILTRADO POR LOCACIONES:')

            # Permitir al usuario ingresar el nombre del archivo
            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES", "L-DEV-CJ-001"])
            # Filtrado por Locacion
            Loc = st.selectbox("Buscar Locacion", options = ["LOCACION", "DEV"])

            if file_name == " " and Loc == " ":
                pass

            if Loc == "DEV":
                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]
                st.dataframe(Ordenar)

                if file_name == "L-DEV-CJ-001" and Loc == "DEV":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)
                        
                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

        else:
            st.write("Por favor, suba un archivo de Excel para visualizarlo.")

    with col2:
        # Instrucciones
        #st.write("Sube varios archivos Excel para combinarlos en uno solo.")
        st.markdown("<h2 style='text-align: center;'>SUBE LOS ARCHIVOS FILTRADOS</h2>", unsafe_allow_html=True)

        # Cargar múltiples archivos
        uploaded_files = st.file_uploader("Elige archivos Excel", type=["xlsx", "xls"], accept_multiple_files=True)

        # Comprobar si se han subido archivos
        if uploaded_files:

            # Ordenar los archivos por nombre, si es necesario
            uploaded_files = sorted(uploaded_files, key=lambda x: x.name)

            dfs = []
            for file in uploaded_files:
                # Leer cada archivo Excel en un DataFrame
                df = pd.read_excel(file)
                dfs.append(df)
                
            # Combinar todos los DataFrames en uno solo
            combined_df = pd.concat(dfs, ignore_index=True)

            # Mostrar el DataFrame combinado
            st.write("DataFrame Combinado:")
            st.dataframe(combined_df)

            # Función para convertir el DataFrame combinado a Excel
            def convert_df_to_excel(df):
                # Crear un objeto BytesIO
                output = BytesIO()
                # Escribir el DataFrame en el objeto BytesIO
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                # Mover el cursor al principio del objeto BytesIO
                output.seek(0)
                return output

            # Convertir DataFrame combinado a Excel
            combined_file = convert_df_to_excel(combined_df)

            # Proporcionar el archivo combinado para descargar
            st.download_button(label="Descargar archivo Excel combinado",
                            data=combined_file,
                            file_name="Filtrado_Final_Files.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.write("Por favor, sube los archivos Excel para combinarlos.")


        # ---------------------------------------------------------------------------------------------------------

elif seleccion == "FILTRADO TOMOS":

    col1, col2 = st.columns(2)
    with col1:
        # Titulo de Aplicacion
        
        st.markdown("<h2 style='text-align: center;'>CARGAR PLANILLA DE EXCEL PARA FILTRAR TOMOS</h2>", unsafe_allow_html=True)

        
        #Cargar el archivo de excel 
        uploaded_file = st.file_uploader('Sube tu archivo de Excel', type=['xlsx','xls'])

        
        if uploaded_file is not None:
            # Leer el archivo Excel usando Pandas
            df = pd.read_excel(uploaded_file, engine='openpyxl')

            # Elimoinar Columnas
            Eliminar = df.drop(['ELIMINAR_1', 'ELIMINAR_2', 'ELIMINAR_3', 'ELIMINAR_4', 'ELIMINAR_5'], axis=1)
            Separar = Eliminar["LOCACION"].str.split('[.-]', expand=True)
            Separar.columns = ['G','LA','P','S','N','L']
            Eliminar = pd.concat([Separar, Eliminar], axis=1)
            Eliminar = Eliminar.drop(['LOCACION'], axis=1)

            # Definimos una ruta para guardar nuestros archivos
            ruta = st.text_input("Introduce la ruta de la carpeta para guardar los Archivos: Obligatorio", "C:\\")
                
            
            # Permitir al usuario ingresar el nombre del archivo
            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES", "Nivel_1", "Nivel_2", "Nivel_3", "Nivel_4", "Nivel_5", "Nivel_6"])

            Nivel = st.selectbox("Buscar Nivel", options = ["NIVEL", "1", "2", "3", "4", "5", "6"])

            if file_name == " " and Nivel == " ":
                pass

            if Nivel == "1":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_1" and Nivel == "1":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                        
                    save_dir = Path(ruta)
                        
                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "2":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_2" and Nivel == "2":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "3":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_3" and Nivel == "3":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


            if Nivel == "4":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_4" and Nivel == "4":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "5":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_5" and Nivel == "5":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "6":

                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'CAJA POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_6" and Nivel == "6":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            
            # Permitir al usuario ingresar el nombre del archivo
            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES", "L-DEV-CJ-001"])
            # Filtrado por Locacion
            Loc = st.selectbox("Buscar Locacion", options = ["LOCACION", "DEV"])

            if file_name == " " and Loc == " ":
                pass

            if Loc == "DEV":
                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)

                if file_name == "L-DEV-CJ-001" and Loc == "DEV":

                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

        else:
            st.write("Por favor, suba un archivo de Excel para visualizarlo.")

    with col2:
        # Instrucciones
        st.markdown("<h2 style='text-align: center;'>SUBE LOS ARCHIVOS FILTRADOS</h2>", unsafe_allow_html=True)

        # Cargar múltiples archivos
        uploaded_files = st.file_uploader("Elige archivos Excel", type=["xlsx", "xls"], accept_multiple_files=True)

        # Comprobar si se han subido archivos
        if uploaded_files:

            # Ordenar los archivos por nombre, si es necesario
            uploaded_files = sorted(uploaded_files, key=lambda x: x.name)

            dfs = []
            for file in uploaded_files:
                # Leer cada archivo Excel en un DataFrame
                df = pd.read_excel(file)
                dfs.append(df)
                
            # Combinar todos los DataFrames en uno solo
            combined_df = pd.concat(dfs, ignore_index=True)

            # Mostrar el DataFrame combinado
            st.write("DataFrame Combinado:")
            st.dataframe(combined_df)

            # Función para convertir el DataFrame combinado a Excel
            def convert_df_to_excel(df):
                # Crear un objeto BytesIO
                output = BytesIO()
                # Escribir el DataFrame en el objeto BytesIO
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                # Mover el cursor al principio del objeto BytesIO
                output.seek(0)
                return output

            # Convertir DataFrame combinado a Excel
            combined_file = convert_df_to_excel(combined_df)

            # Proporcionar el archivo combinado para descargar
            st.download_button(label="Descargar archivo Excel combinado",
                            data=combined_file,
                            file_name="Filtrado_Final_Tomos.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.write("Por favor, sube los archivos Excel para combinarlos.")

            

        # ---------------------------------------------------------------------------------------------------------


elif seleccion == "FILTRADO DE CAJAS":

    col1, col2 = st.columns(2)
    with col1:
        # Titulo de Aplicacion
        
        st.markdown("<h2 style='text-align: center;'>CARGAR PLANILLA DE EXCEL PARA FILTRAR CAJAS</h2>", unsafe_allow_html=True)
        
        #Cargar el archivo de excel 
        uploaded_file = st.file_uploader('Sube tu archivo de Excel', type=['xlsx','xls'])

        
        if uploaded_file is not None:
            # Leer el archivo Excel usando Pandas
            df = pd.read_excel(uploaded_file, engine='openpyxl')

            # Elimoinar Columnas
            Eliminar = df.drop(['ELIMINAR_1', 'ELIMINAR_2', 'ELIMINAR_3', 'ELIMINAR_4', 'ELIMINAR_5','ELIMINAR_6','ELIMINAR_7','ELIMINAR_8'], axis=1)
            Separar = Eliminar["LOCACION"].str.split('[.-]', expand=True)
            Separar.columns = ['G','LA','P','S','N','L']
            Eliminar = pd.concat([Separar, Eliminar], axis=1)
            Eliminar = Eliminar.drop(['LOCACION'], axis=1)

            # Definimos una ruta para guardar nuestros archivos
            ruta = st.text_input("Introduce la ruta de la carpeta para guardar los Archivos: Obligatorio", "C:\\")
            
            # Permitir al usuario ingresar el nombre del archivo
            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES", "Nivel_1", "Nivel_2", "Nivel_3", "Nivel_4", "Nivel_5", "Nivel_6"])

            Nivel = st.selectbox("Buscar Nivel", options = ["NIVEL", "1", "2", "3", "4", "5", "6"])

            if file_name == " " and Nivel == " ":
                pass

            if Nivel == "1":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_1" and Nivel == "1":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    # Definir la ruta de guardado
                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "2":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_2" and Nivel == "2":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "3":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_3" and Nivel == "3":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Nivel == "4":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_4" and Nivel == "4":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


            if Nivel == "5":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_5" and Nivel == "5":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


            if Nivel == "6":
                Ordenar = Eliminar[(Eliminar['N'] == Nivel)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)

                if file_name == "Nivel_6" and Nivel == "6":
                        
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


            # Permitir al usuario ingresar el nombre del archivo
            file_name = st.selectbox("Guardar Como:", options = ["OPCIONES", "L-DEV-CJ-001", "L-PREDESP_IN", "L-PREDESP_EX", "L-ING-CJ-001", "L-INV-CJ-001", "L-SCN-CJ-001", "L-DIG-CJ-001", "L-PALLET"])
            # Filtrado por Locacion
            Loc = st.selectbox("Buscar Locacion", options = ["LOCACION", "DEV", "PREDESP_IN", "PREDESP_EX", "ING", "INV", "SCN", "DIG", "PALLET"])

            if file_name == " " and Loc == " ":
                pass

            if Loc == "DEV":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-DEV-CJ-001" and Loc == "DEV":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "PREDESP_IN":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-PREDESP_IN" and Loc == "PREDESP_IN":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")
                        
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "PREDESP_EX":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-PREDESP_EX" and Loc == "PREDESP_EX":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                        
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "ING":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-ING-CJ-001" and Loc == "ING":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                        
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "INV":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)
                    
                if file_name == "L-INV-CJ-001" and Loc == "INV":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "SCN":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-SCN-CJ-001" and Loc == "SCN":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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

            if Loc == "DIG":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]

                st.dataframe(Ordenar)
                    
                if file_name == "L-DIG-CJ-001" and Loc == "DIG":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                        
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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
                
            if Loc == "PALLET":

                Ordenar = Eliminar[(Eliminar['LA'] == Loc)]
                Ordenar = Ordenar.sort_values(by=['G','LA', 'P', 'S', 'L', 'COD. POLY'])

                st.dataframe(Ordenar)
                    
                if file_name == "L-PALLET" and Loc == "PALLET":
                    # Limpiar el nombre del archivo para evitar caracteres problemáticos
                    file_name = file_name.replace(" ", "_").replace(":", "-").replace("/", "-")

                    
                    save_dir = Path(ruta)

                    # Guardar el DataFrame en un archivo Excel físico
                    file_path =  save_dir / f"{file_name}.xlsx"

                    # Guardar el dataFrame en el archivo Excel
                    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                        Ordenar.to_excel(writer, index=False) # Guardar el primer dataFrame 

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


        else:
            st.write("Por favor, suba un archivo de Excel para visualizarlo.")

    with col2:
        # Instrucciones       
        st.markdown("<h2 style='text-align: center;'>SUBE LOS ARCHIVOS FILTRADOS</h2>", unsafe_allow_html=True)

        # Cargar múltiples archivos
        uploaded_files = st.file_uploader("Elige archivos Excel", type=["xlsx", "xls"], accept_multiple_files=True)

        # Comprobar si se han subido archivos
        if uploaded_files:

            # Ordenar los archivos por nombre, si es necesario
            uploaded_files = sorted(uploaded_files, key=lambda x: x.name)

            dfs = []
            for file in uploaded_files:
                # Leer cada archivo Excel en un DataFrame
                df = pd.read_excel(file)
                dfs.append(df)
                
            # Combinar todos los DataFrames en uno solo
            combined_df = pd.concat(dfs, ignore_index=True)

            # Mostrar el DataFrame combinado
            st.write("DataFrame Combinado:")
            st.dataframe(combined_df)

            # Función para convertir el DataFrame combinado a Excel
            def convert_df_to_excel(df):
                # Crear un objeto BytesIO
                output = BytesIO()
                # Escribir el DataFrame en el objeto BytesIO
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                # Mover el cursor al principio del objeto BytesIO
                output.seek(0)
                return output

            # Convertir DataFrame combinado a Excel
            combined_file = convert_df_to_excel(combined_df)

            # Proporcionar el archivo combinado para descargar
            st.download_button(label="Descargar archivo Excel combinado",
                            data=combined_file,
                            file_name="Filtrado_Final_Cajas.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.write("Por favor, sube los archivos Excel para combinarlos.")
