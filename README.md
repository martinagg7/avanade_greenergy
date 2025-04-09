# 🌱 Greenergy – Simulación de Plataforma Solar

Este proyecto es una simulación de una plataforma inteligente para la empresa **Greenergy**, centrada en la gestión, monitorización y optimización de placas solares mediante dashboards interactivos, lógica simulada de machine learning y detección de fallos. Todo está implementado en **Streamlit** usando datos inventados.



## 📁 Estructura de Páginas

### 🏠 `Home.py` – Página de Inicio

- Bienvenida al sistema Greenergy.
- Métricas simuladas:
  - Producción total (ej. 4235 kWh).
  - Fallos detectados (ej. 3).
  - Eficiencia global (ej. 87.2%).
- Estado general del sistema (mensajes positivos o alertas).
- Imagen ilustrativa de placas solares.


### 📍 `pages/1_Zonas.py` – Gestión de Zonas

- Simula las zonas Norte, Sur, Este y Oeste.
- Permite cambiar la **orientación de placas** con sliders.
- Muestra la **producción estimada** con una fórmula inventada:
  \[
  \text{Producción} = -0.01 \cdot (\text{orientación} - 45)^2 + 100
  \]



### 🤖 `pages/2_Optimizacion.py` – Recomendación Automática

- Simula una recomendación del "modelo de ML".
- Propone orientar todas las placas a 45°.
- Botón para aplicar recomendación (simulado).
- Mensajes sobre el impacto positivo de seguir la recomendación.



### 🛠️ `pages/3_Gadget.py` – Detección de Fallos

- Simula el escaneo de una placa mediante un gadget.
- Selección de placa (ej. "S2", "N3", etc.).
- Muestra si tiene un fallo inventado (ej. “Sobrecalentamiento”, “Fallo inversor”).



### 📊 `pages/4_Informes.py` – Dashboard por Región

- Filtro por país o región (ej. España, Francia, Italia).
- Producción mensual simulada por región.
- Gráfico de barras con producción semanal inventada.
- Se pueden añadir más indicadores por región.



### 💬 `pages/5_Chatbot.py` – Asistente Simulado

- Asistente tipo chatbot con respuestas fijas (reglas simples).
- Contesta a preguntas como:
  - "¿Cuáles son las mejores horas?"
  - "¿Qué hago si hay fallos?"
  - "¿Cuál es la eficiencia?"



### ☀️ `pages/6_Horas_Sol.py` – Optimización por Radiación Solar

- Simula un gráfico de **radiación solar** durante el día.
- Recomienda orientar las placas entre las **11:00 y 15:00**.
- Muestra cómo se puede planificar mejor la producción con datos ambientales.



## 🔧 Dependencias

- `streamlit`
- `numpy`
- `matplotlib`
- (y otras que necesites según funciones añadidas)



## 🚀 Ejecución

```bash
streamlit run Home.py
