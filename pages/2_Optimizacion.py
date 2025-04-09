import streamlit as st
import pandas as pd
import altair as alt

# Configurar página
st.set_page_config(page_title="Optimización - Greenergy", page_icon="⚡", layout="wide")

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
        .card {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #A5D6A7;
            margin-top: 20px;
        }
        .highlight {
            font-size: 24px;
            color: #2E7D32;
            font-weight: 600;
        }
        .impact-msg {
            font-size: 18px;
            margin-top: 20px;
            color: #1B5E20;
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

    <div class="greenergy-title">⚡ Optimización por IA</div>
    <div class="greenergy-subtitle">Recomendación generada por el modelo inteligente de orientación solar</div>
""", unsafe_allow_html=True)

# Mostrar recomendación
st.markdown("""
    <div class="card">
        <p class="highlight">✅ Recomendación actual del modelo:</p>
        <p style="font-size: 18px;">Orienta todas las placas solares a <strong>45°</strong> para maximizar la producción anual.</p>
    </div>
""", unsafe_allow_html=True)

# Botón para aplicar
aplicado = st.button("🚀 Aplicar recomendación de ML")

if aplicado:
    st.success("Recomendación aplicada: orientación ajustada a 45°.")
    st.markdown("""
        <div class="impact-msg">
            📈 Se espera un incremento de hasta <strong>12%</strong> en la producción anual si se mantiene esta orientación constante.
        </div>
    """, unsafe_allow_html=True)

    # Gráfico de barras de impacto
    df = pd.DataFrame({
        "Configuración": ["Actual", "Recomendada (45°)"],
        "Producción estimada (kWh)": [1000, 1120]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Configuración", sort=None),
        y="Producción estimada (kWh)",
        color=alt.condition(
            alt.datum.Configuración == "Recomendada (45°)",
            alt.value("#66BB6A"),
            alt.value("#BDBDBD")
        )
    ).properties(
        title="Impacto estimado en la producción anual",
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Puedes aplicar esta recomendación con el botón de arriba para simular su efecto.")

# Botón de retorno al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
