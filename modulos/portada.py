# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
figlet = Figlet(font='standard')  # Puedes probar 'standard', 'big', 'banner3-D', etc.

# Texto que quieres mostrar
texto = "JC DEV SISTEM"

# Convertir a ASCII art
ascii_art = figlet.renderText(texto)

# Mostrar en Streamlit centrado, con color neón y sombra
st.markdown(f"""
<div style="
    text-align: center;
    color: #00ffff;
    font-size: 24px;
    font-family: monospace;
    white-space: pre;
    text-shadow: 2px 2px 5px #00ffff, 0 0 10px #00ffff, 0 0 20px #00ffff;
">
{ascii_art}
 """, 
unsafe_allow_html=True)
   

st.markdown("""
<div style="width: 100%; overflow: hidden; white-space: nowrap;">
<div style="
    display: inline-block;
    padding-left: 120%;
    animation: scroll-left 15s linear infinite;
    font-size: 18px;
    color: #3498db;
">
    DERECHOS-RECERVADOS - @JUAN CARLOS RAMOS CHURA - 2026
</div>
</div>

<style>
@keyframes scroll-left {
0%   { transform: translateX(0%); }
100% { transform: translateX(-100%); }
}
</style>
""", unsafe_allow_html=True)
