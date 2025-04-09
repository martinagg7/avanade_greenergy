import streamlit as st
from pathlib import Path

# Configurar la página
st.set_page_config(
    page_title="Greenergy",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={}
)

# Estilo visual profesional
st.markdown("""
    <style>
        .main-container {
            text-align: center;
        }
        .greenergy-title {
            font-size: 44px;
            color: #2E7D32;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .greenergy-subtitle {
            font-size: 20px;
            color: #4CAF50;
            margin-top: 0;
        }
        .button-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 22px;
            margin-top: 2rem;
        }
        .button-link {
            background-color: #E8F5E9;
            padding: 16px 26px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: 500;
            color: #2E7D32 !important;
            border: 2px solid #A5D6A7;
            box-shadow: 1px 2px 5px rgba(0,0,0,0.05);
            text-decoration: none !important;
            transition: all 0.2s ease;
        }
        .button-link:hover {
            background-color: #C8E6C9;
            transform: scale(1.03);
            box-shadow: 2px 3px 10px rgba(0,0,0,0.1);
        }
    </style>

    <div class="main-container">
        <div class="greenergy-title">🌱 Greenergy</div>
        <div class="greenergy-subtitle">Sistema inteligente de gestión de energía solar</div>
        <hr style="width: 50%; margin: 1.5rem auto;">
""", unsafe_allow_html=True)

# Imagen centrada y más compacta
img_path = Path(__file__).parent / "1.png"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(img_path, width=620)

st.markdown("</div>", unsafe_allow_html=True)

# Botones de navegación estilizados
st.markdown("### 🔎 ¿Qué deseas hacer hoy?")
st.markdown("""
    <div class="button-container">
        <a class="button-link" href="pages/1_Zonas.py">🌍 Zonas</a>
        <a class="button-link" href="pages/2_Optimizacion.py">⚡ Optimización</a>
        <a class="button-link" href="pages/3_Gadget.py">🔧Gadget</a>
        <a class="button-link" href="pages/4_Informes.py">📑 Informes</a>
        <a class="button-link" href="pages/6_Horas_Sol.py">☀️ Horas de Sol</a>
        <a class="button-link" href="pages/5_Chatbot.py">🤖 Chatbot</a>
    </div>
""", unsafe_allow_html=True)

# Footer limpio
st.markdown("<hr style='width: 50%;'>", unsafe_allow_html=True)
st.caption("© 2025 Greenergy. Desarrollado por Avanade.")
