import streamlit as st
import random

# Configurar página
st.set_page_config(page_title="Gadget - Greenergy", page_icon="🔧", layout="wide")

# Estilo profesional
st.markdown("""
    <style>
        .greenergy-title {
            font-size: 36px;
            color: #2E7D32;
            font-weight: bold;
            text-align: center;
        }
        .greenergy-subtitle {
            font-size: 20px;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 30px;
        }
        .result-card {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #A5D6A7;
            margin-top: 20px;
            text-align: center;
        }
        .result-ok {
            color: #388E3C;
            font-size: 22px;
            font-weight: 600;
        }
        .result-fail {
            color: #C62828;
            font-size: 22px;
            font-weight: 600;
        }
        .return-link {
            display: block;
            width: fit-content;
            margin: 40px auto 10px auto;
            background-color: #E8F5E9;
            padding: 14px 24px;
            border-radius: 12px;
            border: 2px solid #A5D6A7;
            font-size: 18px;
            font-weight: 500;
            color: #2E7D32 !important;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }
        .return-link:hover {
            background-color: #C8E6C9;
            transform: scale(1.03);
        }
    </style>

    <div class="greenergy-title">🔧 Gadget de Diagnóstico</div>
    <div class="greenergy-subtitle">Escanea una placa solar para detectar posibles fallos</div>
""", unsafe_allow_html=True)

# Selección de placa
placas = [f"N{i}" for i in range(1, 6)] + [f"S{i}" for i in range(1, 6)]
placa = st.selectbox("Selecciona una placa solar para escanear:", placas)

# Simulación de fallos
fallos_posibles = ["Sobrecalentamiento", "Fallo inversor", "Bajo voltaje", "Panel sucio", "Sin fallos detectados"]

# Botón para escanear
if st.button("🔍 Escanear placa"):
    fallo = random.choice(fallos_posibles)
    if fallo == "Sin fallos detectados":
        st.markdown(f"""
            <div class="result-card">
                <p class="result-ok">✅ Placa {placa} escaneada correctamente. Sin fallos detectados.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="result-card">
                <p class="result-fail">⚠️ Placa {placa} presenta un fallo: <strong>{fallo}</strong></p>
            </div>
        """, unsafe_allow_html=True)

# Botón de retorno al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
