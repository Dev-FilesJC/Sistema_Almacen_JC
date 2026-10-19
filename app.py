# ======================================================
# SISTEMA ALMACEN - DESPACHO LA PAZ
# JC CODE SISTEM - VERSION CENTRADA PROFESIONAL
# ======================================================

import streamlit as st
import warnings
import plotly.express as px
import pandas as pd
import os
import plotly.graph_objects as go
import xlsxwriter
from pathlib import Path
import glob
from io import BytesIO
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.drawing.image import Image as OpenpyxlImage
from datetime import datetime
from pyfiglet import Figlet


warnings.filterwarnings("ignore")

# ==============================
# CONFIGURACIÓN
# ==============================
st.set_page_config(
    page_title="Sistema Almacen - Despacho La Paz",
    page_icon="📦",
    #layout="centered",
    layout="wide",
    initial_sidebar_state="expanded"  # 👈 SIDEBAR VISIBLE
)

# ==============================
# CSS PROFESIONAL
# ==============================
st.markdown("""
<style>

/* ===== OCULTAR ELEMENTOS STREAMLIT ===== */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ===== FONDO GENERAL ===== */
.stApp {
    background: linear-gradient(135deg, #0e1117, #161b22);
}

/* ===== CONTENIDO CENTRADO ===== */
.block-container {
            
    max-width: 100%;
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* ===== LOGIN ===== */
.login-wrapper {
    height: 15vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.login-box {
    background-color: #161b22;
    padding: 40px;
    border-radius: 15px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
}

.login-title {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}

.login-sub {
    text-align: center;
    color: #8b949e;
    margin-bottom: 25px;
}

/* ===== INPUTS ===== */
div[data-testid="stTextInput"] {
    max-width: 600px;   /* 👈 Cambia el tamaño aquí */
    margin: auto;       /* 👈 Lo centra */
}
.stTextInput>div>div>input {
    background-color: #0d1117;
    color: white;
    border-radius: 8px;
}

/* ===== BOTONES ===== */
div[data-testid="stButton"] {
    max-width: 250px;   /* 👈 cambia el ancho aquí */
    margin-left: auto;
    margin-right: auto;
}
.stButton>button {
    background-color: #238636;
    color: white;
    border-radius: 8px;
    height: 40px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #2ea043;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background-color: #161b22;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# ==============================
# USUARIOS Y PERMISOS
# ==============================
# Las cuentas y contraseñas se cargan desde Streamlit Community Cloud > Settings > Secrets.
# No escribas contraseñas aquí ni subas un archivo secrets.toml a GitHub.
try:
    USUARIOS = {
        str(nombre): {
            "password": str(datos["password"]),
            "rol": str(datos["rol"]),
        }
        for nombre, datos in st.secrets["usuarios"].items()
    }
    if not USUARIOS:
        raise ValueError("La sección [usuarios] está vacía.")
except Exception:
    st.error("No se configuraron los usuarios en Streamlit Secrets.")
    st.markdown(
        "Abre tu aplicación en Streamlit Community Cloud → **Settings** → **Secrets** "
        "y copia la estructura del archivo `SECRETS_EJEMPLO.toml` incluido en el proyecto."
    )
    st.stop()

PERMISOS = {
    "admin": [
        "PORTADA",
        "FILTRADOR ALMACEN",
        "CALENDARIO ALMACEN",
        "CREAR GUIA RUTA LA PAZ",
        "CHECK FILEWEB AND LASERFICHE",
        "SINTAXIS LASERFICHE-ONEIL",
        "DUPLICAR FILAS",
        "SEPARADOR ITEMS ONEIL",
        "JUEGA CON DINO"
    ],
    "despacho": [
        "PORTADA",
        "FILTRADOR ALMACEN",
        "SEPARADOR ITEMS ONEIL"
        
    ],
    "despacho2": [
        "PORTADA",
        "FILTRADOR ALMACEN",
        "CALENDARIO ALMACEN",
        "SEPARADOR ITEMS ONEIL"
    ]
}

# Evitar que una cuenta configurada con un rol inexistente cause un error en el menú.
roles_invalidos = sorted({datos["rol"] for datos in USUARIOS.values() if datos["rol"] not in PERMISOS})
if roles_invalidos:
    st.error("Hay usuarios con roles no reconocidos en Streamlit Secrets: " + ", ".join(roles_invalidos))
    st.stop()

# ==============================
# SESSION STATE
# ==============================
if "login" not in st.session_state:
    st.session_state.login = False

# ==============================
# LOGIN
# ==============================
if not st.session_state.login:

    st.markdown("<div class='login-wrapper'>", unsafe_allow_html=True)
    #st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("<div class='login-title'>🔐 JC DEV_SISTEM</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>SISTEMA ALMACEN DESPACHO LA PAZ</div>", unsafe_allow_html=True)

    usuario = st.text_input("👤 Usuario")
    password = st.text_input("🔑 Contraseña", type="password")

    if st.button("Ingresar", use_container_width=True):
        if usuario in USUARIOS and USUARIOS[usuario]["password"] == password:
            st.session_state.login = True
            st.session_state.usuario = usuario
            st.session_state.rol = USUARIOS[usuario]["rol"]
            st.rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos")

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.stop()

# ==============================
# SIDEBAR
# ==============================
st.sidebar.markdown(
    "<h1 style='text-align:center; color:white;'>📦 JC CODE SISTEM</h1>",
    unsafe_allow_html=True
)

st.sidebar.write(f"👤 Usuario: **{st.session_state.usuario}**")
st.sidebar.write(f"🔐 Rol: **{st.session_state.rol}**")

if st.sidebar.button("Cerrar sesión"):
    st.session_state.clear()
    st.rerun()

st.sidebar.markdown("---")

opciones = PERMISOS[st.session_state.rol]
proyecto = st.sidebar.selectbox("Seleccione una opción", opciones)



# ==============================
# CONTENIDO PRINCIPAL
# ==============================
st.title("📁 SISTEMA ALMACEN LA PAZ - BOLIVIA")

from modulos.page_router import render_page
render_page(proyecto, globals())

