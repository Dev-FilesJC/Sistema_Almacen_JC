# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import streamlit as st
from datetime import datetime
    
st.subheader("🧠 SINTAXIS LASERFICHE-ONEIL")
    
# --------------------- SIDEBAR MENU ---------------------
st.sidebar.title("Menú de Opciones")
menu = st.sidebar.radio("Ir a:", [
    "🧱 OTPM - MATERIALES",
    "🗃️ OTEX - EXTRACIONES",
    "📤 OTEV - ENVIO",
    "📥 OTRE - RECOJO",
    "✉️ OTRE - POR_WORKORDERS",
    "🧾 OTRE - POR_SOLICITUDES",
    "📝 OTRE - SOLICITUDES",
    "🧠 COD - BASE_DE_DATO",
    "🎨 CONTENIDO_PALLETS",
    "🔖 CODIGOS DE 6 DIGITOS"
        
])
def OTPM_MATERIALES():
        
    opciones2 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

    # Crear el menu desplegable con st.selectbox()
    seleccion2 = st.selectbox("Selecciona una opcion del menu: ", opciones2)

    if seleccion2 == "PENDIENTE":
        #import streamlit as st
        from datetime import datetime
            
        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\01. OTPM - Preparación de Materiales\\03. Finalizada\\01. Pendiente"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                        
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()
    
    elif seleccion2 == "EN PROCESO":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\01. OTPM - Preparación de Materiales\\02. En Proceso"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                        
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()

    elif seleccion2 == "FINALIZADA":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\01. OTPM - Preparación de Materiales\\03. Finalizada"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                        
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()
        
    elif seleccion2 == "ANULADA":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\01. OTPM - Preparación de Materiales\\04. Anulada"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                        
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()

def OTEX_EXTRACIONES():

    # Crear una lista de opciones para el menu 
    opciones3 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

    # Crear el menu desplegable con st.selectbox()
    seleccion3 = st.selectbox("Selecciona una opcion del menu: ", opciones3)

    if seleccion3 == "PENDIENTE":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\06. OTEX - Extracción\\01. Pendiente"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()


    elif seleccion3 == "EN PROCESO":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\06. OTEX - Extracción\\02. En proceso"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()

    elif seleccion3 == "FINALIZADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\06. OTEX - Extracción\\03. Finalizada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

    elif seleccion3 == "ANULADA":
        #import streamlit as st
        from datetime import datetime

        def main():
            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Sintaxis predeterminada
            sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\06. OTEX - Extracción\\04. Anulada"}'

            # Sección para seleccionar una fecha usando un calendario
            st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
            fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                # Formatear la fecha seleccionada
                fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                # Mostrar la sintaxis generada
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

        if __name__ == "__main__":
            main()

def OTEV_ENVIO():

    # Crear una lista de opciones para el menu 
    opciones2 = ["SELECCIONA UNA OPCION", "INTERNO", "EXTERNO"]

    # Crear el menu desplegable con st.selectbox()
    seleccion2 = st.selectbox("Selecciona una opcion del menu: ", opciones2)

    if seleccion2 == "INTERNO":
        # Crear una lista de opciones para el menu 
        opciones3 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

        # Crear el menu desplegable con st.selectbox()
        seleccion3 = st.selectbox("Selecciona una opcion del menu: ", opciones3)

        if seleccion3 == "PENDIENTE":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Interno\\01. Pendiente"}'

                # Sección para seleccionar una fecha usando un calendariO
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()


        elif seleccion2 == "EN PROCESO":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Interno\\02. En proceso"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion2 == "FINALIZADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Interno\\03. Finalizada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                    main()

        elif seleccion2 == "ANULADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Interno\\04. Anulada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

    if seleccion2 == "EXTERNO":
        # Crear una lista de opciones para el menu 
        opciones3 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

        # Crear el menu desplegable con st.selectbox()
        seleccion3 = st.selectbox("Selecciona una opcion del menu: ", opciones3)

        if seleccion3 == "PENDIENTE":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Externo\\01. Pendiente"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()


        elif seleccion3 == "EN PROCESO":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Externo\\02. En proceso"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "FINALIZADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Externo\\03. Finalizada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "ANULADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTEV - Envío\\01. Solicitante Externo\\04. Anulada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

def OTRE_RECOJO():

    # Crear una lista de opciones para el menu 
    opciones2 = ["SELECCIONA UNA OPCION", "INTERNO", "EXTERNO"]

    # Crear el menu desplegable con st.selectbox()
    seleccion2 = st.selectbox("Selecciona una opcion del menu: ", opciones2)

    if seleccion2 == "INTERNO":
        # Crear una lista de opciones para el menu 
        opciones3 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

        # Crear el menu desplegable con st.selectbox()
        seleccion3 = st.selectbox("Selecciona una opcion del menu: ", opciones3)

        if seleccion3 == "PENDIENTE":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\01. Solicitante Interno\\01. Pendiente"}'

                # Sección para seleccionar una fecha usando un calendario
                st.header("Seleccione una fecha")
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()


        elif seleccion3 == "EN PROCESO":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\01. Solicitante Interno\\02. En proceso"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "FINALIZADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\01. Solicitante Interno\\03. Finalizada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "ANULADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\01. Solicitante Interno\\04. Anulada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

    if seleccion2 == "EXTERNO":
        # Crear una lista de opciones para el menu 
        opciones3 = ["SELECCIONA UNA OPCION", "PENDIENTE", "EN PROCESO", "FINALIZADA", "ANULADA"]

        # Crear el menu desplegable con st.selectbox()
        seleccion3 = st.selectbox("Selecciona una opcion del menu: ", opciones3)

        if seleccion3 == "PENDIENTE":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\02. Solicitante Externo\\01. Pendiente"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()


        elif seleccion3 == "EN PROCESO":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\02. Solicitante Externo\\02. En proceso"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "FINALIZADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\02. Solicitante Externo\\03. Finalizada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

        elif seleccion3 == "ANULADA":
            #import streamlit as st
            from datetime import datetime

            def main():
                st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

                # Sintaxis predeterminada
                sintaxis_predeterminada = '{LF:LOOKIN="PolyfilesBO\\02. Ordenes de Trabajo\\03. OTRE - Recojo\\02. Solicitante Externo\\04. Anulada"}'

                # Sección para seleccionar una fecha usando un calendario
                st.markdown("<h4>Seleccione una fecha </h4>", unsafe_allow_html=True)
                fecha_input = st.date_input("Fecha de creación:", value=datetime.today())

                # Variable para almacenar la sintaxis generada
                sintaxis_final = ""

                # Generar la sintaxis de búsqueda
                if st.button("Generar Sintaxis"):
                    # Formatear la fecha seleccionada
                    fecha_formateada = fecha_input.strftime("%d/%m/%Y")
                    sintaxis_final = f"{sintaxis_predeterminada} & {{LF:Created=\"{fecha_formateada}\"}}"
                            
                    # Mostrar la sintaxis generada
                    st.success("Sintaxis de búsqueda generada:")
                    st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

            if __name__ == "__main__":
                main()

def OTRE_POR_WORKORDERS():
    #import streamlit as st
    from datetime import datetime

    def main():
        col1, col2 = st.columns((2))
        with col1:

            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Cargar archivo de texto
            st.markdown("<h4>Selecciona el archivo de texto con Nros de WOs </h4>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecciona un archivo .txt", type="txt")

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                        
                # Leer el archivo y extraer los Nros de WO
                if uploaded_file is not None:
                    content = uploaded_file.read().decode("utf-8")
                    wo_numbers = content.splitlines()  # Suponiendo que cada WO está en una línea

                    # Crear la parte de la sintaxis para los Nros de WO
                    wo_sintaxis = " | ".join([f'\n{{[Orden de Trabajo]:[Nro de WO]="{wo.strip()}"}}' for wo in wo_numbers if wo.strip()])

                    # Construir la sintaxis final
                    sintaxis_final = f"{wo_sintaxis}"

        with col2:

            # Mostrar la sintaxis generada
            if sintaxis_final:
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

                # ==============================
                # 🔽 Botón para descargar archivo
                # ==============================
                st.download_button(
                    label="📥 Descargar archivo",
                    data=sintaxis_final,
                    file_name=f"sintaxis_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain"
                )

                        
    if __name__ == "__main__":
        main()

def OTRE_POR_SOLICITUDES():
    #import streamlit as st
    from datetime import datetime

    def main():
        col1, col2 = st.columns((2))
        with col1:

            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Cargar archivo de texto
            st.markdown("<h4>Selecciona el archivo de texto con Nros de Solicitudes </h4>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecciona un archivo .txt", type="txt")

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                        
                # Leer el archivo y extraer los Nros de WO
                if uploaded_file is not None:
                    content = uploaded_file.read().decode("utf-8")
                    wo_numbers = content.splitlines()  # Suponiendo que cada WO está en una línea

                    # Crear la parte de la sintaxis para los Nros de WO
                    wo_sintaxis = " | ".join([f'\n{{[Orden de Trabajo]:[Nro Solicitud]="{wo.strip()}"}}' for wo in wo_numbers if wo.strip()])

                    # Construir la sintaxis final
                    sintaxis_final = f"{wo_sintaxis}"

        with col2:

            # Mostrar la sintaxis generada
            if sintaxis_final:
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

                # ==============================
                # 🔽 Botón para descargar archivo
                # ==============================
                st.download_button(
                    label="📥 Descargar archivo",
                    data=sintaxis_final,
                    file_name=f"sintaxis_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain"
                )

                        
    if __name__ == "__main__":
        main()
 
def OTRE_SOLICITUDES():
    #import streamlit as st
    from datetime import datetime

    def main():
        col1, col2 = st.columns((2))
        with col1:

            st.markdown("<h3>Generador de Sintaxis de Busqueda </h3>", unsafe_allow_html=True)

            # Cargar archivo de texto
            st.markdown("<h4>Selecciona el archivo de texto con Nros de SOLICITUDES </h4>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecciona un archivo .txt", type="txt")

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                        
                # Leer el archivo y extraer los Nros de WO
                if uploaded_file is not None:
                    content = uploaded_file.read().decode("utf-8")
                    solicitud_numbers = content.splitlines()  # Suponiendo que cada WO está en una línea

                    # Crear la parte de la sintaxis para los Nros de WO
                    solicitud_sintaxis = " | ".join([f'\n{{[Solicitud]:[Nro Solicitud]="{solicitud.strip()}"}}' for solicitud in solicitud_numbers if solicitud.strip()])

                    # Construir la sintaxis final
                    sintaxis_final = f"{solicitud_sintaxis}"

        with col2:

            # Mostrar la sintaxis generada
            if sintaxis_final:
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

                # ==============================
                # 🔽 Botón para descargar archivo
                # ==============================
                st.download_button(
                    label="📥 Descargar archivo",
                    data=sintaxis_final,
                    file_name=f"sintaxis_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain"
                )  

    if __name__ == "__main__":
        main()

def COD_BASE_DE_DATO():
    #import streamlit as st
    from datetime import datetime

    def main():
        col1, col2 = st.columns((2))
        with col1:

            st.markdown("<h3>Generador de Codigos para descargar BD </h3>", unsafe_allow_html=True)

            # Cargar archivo de texto
            st.markdown("<h4>Selecciona el archivo de texto con Codigos Poly </h4>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecciona un archivo .txt", type="txt")

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                        
                # Leer el archivo y extraer los Nros de WO
                if uploaded_file is not None:
                    content = uploaded_file.read().decode("utf-8")
                    solicitud_numbers = content.splitlines()  # Suponiendo que cada WO está en una línea

                    # Crear la parte de la sintaxis para los Nros de WO
                    solicitud_sintaxis = " OR ".join([f'\n Filefolder^ContainerCode = "{solicitud.strip()}"' for solicitud in solicitud_numbers if solicitud.strip()])
                    # Construir la sintaxis final
                    sintaxis_final = f"{solicitud_sintaxis}"

        with col2:

            # Mostrar la sintaxis generada
            if sintaxis_final:
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

                # ==============================
                # 🔽 Botón para descargar archivo
                # ==============================
                st.download_button(
                    label="📥 Descargar archivo",
                    data=sintaxis_final,
                    file_name=f"sintaxis_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain"
                )

    if __name__ == "__main__":
        main()

def CONTENIDO_PALLETS():
    #import streamlit as st
    from datetime import datetime

    def main():
        col1, col2 = st.columns((2))
        with col1:

            st.markdown("<h3>Generador de Piso Pallets para ver contenido </h3>", unsafe_allow_html=True)

            # Cargar archivo de texto
            st.markdown("<h4>Selecciona el archivo de texto con Locaciones de Pallets </h4>", unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Selecciona un archivo .txt", type="txt")

            # Variable para almacenar la sintaxis generada
            sintaxis_final = ""

            # Generar la sintaxis de búsqueda
            if st.button("Generar Sintaxis"):
                        
                # Leer el archivo y extraer los Nros de WO
                if uploaded_file is not None:
                    content = uploaded_file.read().decode("utf-8")
                    solicitud_numbers = content.splitlines()  # Suponiendo que cada WO está en una línea

                    # Crear la parte de la sintaxis para los Nros de WO
                    #solicitud_sintaxis = " | ".join([f'\n{{[Solicitud]:[Nro Solicitud]="{solicitud.strip()}"}}' for solicitud in solicitud_numbers if solicitud.strip()])
                    solicitud_sintaxis = " OR ".join([f'\n Container^LocationCode = "{solicitud.strip()}"' for solicitud in solicitud_numbers if solicitud.strip()])
                    # Construir la sintaxis final
                    sintaxis_final = f"{solicitud_sintaxis}"

        with col2:

            # Mostrar la sintaxis generada
            if sintaxis_final:
                st.success("Sintaxis de búsqueda generada:")
                st.code(sintaxis_final)  # Muestra la sintaxis en un bloque de código

                # ==============================
                # 🔽 Botón para descargar archivo
                # ==============================
                st.download_button(
                    label="📥 Descargar archivo",
                    data=sintaxis_final,
                    file_name=f"sintaxis_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain"
                )

    if __name__ == "__main__":
            main()

def CODIGOS_DE_6_DIGITOS():
    import pandas as pd
    from io import StringIO

    st.title("📄 Completar códigos a 6 dígitos con ceros")

    st.markdown("""
    Sube un archivo `.txt` que contenga un código por línea.  
    Este script completará cada código a **6 dígitos** rellenando con ceros a la izquierda.
    """)

    uploaded_file = st.file_uploader("📤 Cargar archivo TXT", type=["txt"])

    if uploaded_file is not None:
        # Leer el archivo como texto
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        lines = stringio.readlines()

        # Eliminar saltos de línea y espacios extra
        codes = [line.strip() for line in lines if line.strip()]

        # Completar con ceros a la izquierda
        completed_codes = [code.zfill(6) for code in codes]

        # Mostrar los primeros 5 códigos
        st.subheader("🔍 Vista previa (primeras 5 filas):")
        preview = completed_codes[:5]
        df_preview = pd.DataFrame(preview, columns=["Código Completado"])
        st.dataframe(df_preview, use_container_width=True)

        # Mostrar todos los resultados (colapsable)
        with st.expander("📋 Ver todos los códigos completados"):
            st.code("\n".join(completed_codes), language='text')

        # Campo para que el usuario ingrese el nombre del archivo de descarga
        filename = st.text_input(
            "✏️ Nombre del archivo de salida (sin extensión):",
            value="codigos_completados"
        )

        # Botón de descarga
        output_text = "\n".join(completed_codes)
        if filename.strip():
            st.download_button(
                label="⬇️ Descargar archivo procesado",
                data=output_text,
                file_name=f"{filename.strip()}.txt",
                mime="text/plain"
            )
    else:
        st.info("Por favor, sube un archivo `.txt` para procesarlo.")

            
    # --------------------- EJECUTAR SEGÚN MENÚ ---------------------
        
if menu == "🧱 OTPM - MATERIALES":
    OTPM_MATERIALES()
elif menu == "🗃️ OTEX - EXTRACIONES":
    OTEX_EXTRACIONES()
elif menu == "📤 OTEV - ENVIO":
    OTEV_ENVIO()
elif menu == "📥 OTRE - RECOJO":
    OTRE_RECOJO()
elif menu == "✉️ OTRE - POR_WORKORDERS":
    OTRE_POR_WORKORDERS()
elif menu == "🧾 OTRE - POR_SOLICITUDES":
    OTRE_POR_SOLICITUDES()
elif menu == "📝 OTRE - SOLICITUDES":
    OTRE_SOLICITUDES()
elif menu == "🧠 COD - BASE_DE_DATO":
    COD_BASE_DE_DATO()
elif menu == "🎨 CONTENIDO_PALLETS":
    CONTENIDO_PALLETS()  
elif menu == "🔖 CODIGOS DE 6 DIGITOS":
    CODIGOS_DE_6_DIGITOS()
