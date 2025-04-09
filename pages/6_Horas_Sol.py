import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Configurar página
st.set_page_config(page_title="Horas de Sol - Greenergy", page_icon="☀️", layout="wide")

# Estilo visual profesional
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
        .advice-card {
            background-color: #FFFDE7;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #FDD835;
            margin-top: 20px;
        }
        .advice {
            font-size: 20px;
            font-weight: 500;
            color: #F9A825;
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

    <div class="greenergy-title">🔆 Horas de Sol</div>
    <div class="greenergy-subtitle">Visualización de la radiación solar diaria para una mejor planificación energética</div>
""", unsafe_allow_html=True)

# Simular datos de radiación solar a lo largo del día (6h a 20h)
horas = list(range(6, 21))
radiacion = [round(800 * np.exp(-((h - 13) ** 2) / 8), 1) for h in horas]  # pico a las 13h

df = pd.DataFrame({
    "Hora": [f"{h}:00" for h in horas],
    "Radiación Solar (W/m²)": radiacion
})

# Gráfico
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Hora",
    y="Radiación Solar (W/m²)",
    color=alt.value("#FBC02D")
).properties(
    title="Radiación solar estimada a lo largo del día",
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)

# Recomendación
st.markdown("""
    <div class="advice-card">
        <p class="advice">🌞 Se recomienda orientar las placas entre las <strong>11:00 y 15:00</strong> para aprovechar el pico de radiación solar.</p>
    </div>
""", unsafe_allow_html=True)

# Explicación adicional
st.markdown("### 🧠 ¿Por qué es útil esto?")
st.markdown("""
- Los datos ambientales permiten predecir la **producción esperada**.
- Saber cuándo ocurre el **pico de radiación** ayuda a:
    - Optimizar el ángulo de inclinación
    - Gestionar mejor el almacenamiento
    - Priorizar tareas de mantenimiento fuera del horario crítico
""")

# Volver al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
