import streamlit as st

# Configurar página
st.set_page_config(page_title="Chatbot - Greenergy", page_icon="🤖", layout="wide")

# Estilo visual
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
        .chat-bubble {
            background-color: #E8F5E9;
            padding: 14px 20px;
            border-radius: 12px;
            margin: 10px 0;
            width: fit-content;
            max-width: 80%;
        }
        .user {
            margin-left: auto;
            background-color: #C8E6C9;
        }
        .bot {
            margin-right: auto;
            background-color: #F1F8E9;
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

    <div class="greenergy-title">🤖 Asistente Solar</div>
    <div class="greenergy-subtitle">Consulta rápida sobre producción, fallos y eficiencia</div>
""", unsafe_allow_html=True)

# Entrada del usuario
pregunta = st.text_input("💬 Escribe tu pregunta:")

# Reglas de respuesta
respuestas = {
    "mejores horas": "🌞 Las mejores horas para producción solar son entre las 11:00 y 15:00.",
    "fallos": "🔧 Si detectas un fallo, revisa el gadget de diagnóstico y agenda mantenimiento.",
    "eficiencia": "📈 La eficiencia promedio de los paneles es de un 18% a 22% según condiciones óptimas.",
    "recomendación": "⚡ Puedes aplicar la orientación recomendada de 45° desde la sección de Optimización.",
    "zonas": "🧭 Puedes estimar producción según la zona (Norte, Sur, Este, Oeste) en la sección Zonas."
}

if pregunta:
    # Mostrar pregunta del usuario
    st.markdown(f"<div class='chat-bubble user'>{pregunta}</div>", unsafe_allow_html=True)

    # Buscar respuesta
    matched = False
    for clave, respuesta in respuestas.items():
        if clave in pregunta.lower():
            st.markdown(f"<div class='chat-bubble bot'>{respuesta}</div>", unsafe_allow_html=True)
            matched = True
            break

    if not matched:
        st.markdown(f"<div class='chat-bubble bot'>🤔 Lo siento, no tengo una respuesta para eso. Intenta con otra pregunta.</div>", unsafe_allow_html=True)

# Ayuda para el usuario
st.markdown("""
<details>
<summary>❓ Preguntas frecuentes que puedes probar</summary>

- ¿Cuáles son las mejores horas?
- ¿Qué hago si hay fallos?
- ¿Cuál es la eficiencia?
- ¿Cuál es la recomendación?
- ¿Qué zonas son mejores?
</details>
""", unsafe_allow_html=True)

# Retorno al home
st.markdown("""
    <a class="return-link" href="../home.py">⬅️ Volver al inicio</a>
""", unsafe_allow_html=True)
