import streamlit as st
import pandas as pd
import random
import altair as alt

# Configurar página
st.set_page_config(page_title="Informes - Greenergy", page_icon="📑", layout="wide")

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
        .info-card {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #A5D6A7;
            text-align: center;
            margin-bottom: 30px;
        }
        .indicator {
            font-size: 24px;
            color: #2E7D32;
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

    <div class="greenergy-title">📊 Informes por Región</div>
    <div class="greenergy-subtitle">Visualiza la producción mensual y semanal por país</div>
""", unsafe_allow_html=True)

# Filtro de región
region = st.selectbox("Selecciona una región", ["España", "Francia", "Italia"])

# Simular datos
produccion_mensual = random.randint(4000, 8000)  # kWh
produccion_semanal = [random.randint(900, 2200) for _ in range(4)]

# Mostrar producción mensual
st.markdown(f"""
    <div class="info-card">
        <p class="indicator">📆 Producción mensual estimada en {region}: <strong>{produccion_mensual} kWh</strong></p>
    </div>
""", unsafe_allow_html=True)

# Gráfico de producción semanal
df = pd.DataFrame({
    "Semana": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
    "Producción (kWh)": produccion_semanal
})

chart = alt.Chart(df).mark_bar().encode(
    x="Semana",
    y="Producción (kWh)",
    color=alt.value("#66BB6A")
).properties(
    title=f"Producción semanal en {region}",
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

# Espacio para más indicadores
with st.expander("📌 Indicadores adicionales (futuros):"):
    st.markdown("- Comparativa anual por país")
    st.markdown("- Eficiencia promedio por planta")
    st.markdown("- Emisiones evitadas (CO₂)")
    st.markdown("- Ranking de rendimiento")

# Botón de retorno al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
