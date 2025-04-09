import streamlit as st
import math

# Configurar página
st.set_page_config(page_title="Zonas - Greenergy", page_icon="🌍", layout="wide")

# Estilo visual consistente
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
        .zona-card {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #A5D6A7;
        }
        .highlight {
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

    <div class="greenergy-title">📍 Zonas de la Planta Solar</div>
    <div class="greenergy-subtitle">Selecciona la orientación y ajusta la inclinación para estimar la producción</div>
""", unsafe_allow_html=True)

# Zona cardinal
zona = st.selectbox("Selecciona la zona de orientación solar", ["Norte", "Sur", "Este", "Oeste"])

# Slider de orientación (ángulo)
angulo = st.slider("Ángulo de inclinación de los paneles (0° = horizontal, 90° = vertical)", min_value=0, max_value=90, value=30)

# Factores por zona
zona_factor_dict = {
    "Norte": 0.85,
    "Sur": 1.0,
    "Este": 0.9,
    "Oeste": 0.92
}
zona_factor = zona_factor_dict[zona]

# Cálculo de producción (fórmula inventada)
base_produccion = 1000  # kWh base
factor_orientacion = math.cos(math.radians(angulo))  # eficiencia por inclinación
produccion_estim = base_produccion * factor_orientacion * zona_factor

# Mostrar resultado
st.markdown(f"""
    <div class="zona-card">
        <p><strong>Zona seleccionada:</strong> {zona}</p>
        <p><strong>Ángulo:</strong> {angulo}°</p>
        <p class="highlight">🔋 Producción estimada: {produccion_estim:.2f} kWh</p>
    </div>
""", unsafe_allow_html=True)

# Botón de retorno al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
