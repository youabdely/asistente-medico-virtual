import streamlit as st
import openai
import os

# Obtiene la API key desde los secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

modelo = "gpt-4-1106-preview"

st.set_page_config(page_title="Asistente Médico Virtual", page_icon="🩺")
st.title("🩺 Asistente Médico Virtual")

st.markdown("Escribe tu consulta médica y recibirás una respuesta orientativa. No sustituye a un profesional de la salud.")

user_input = st.text_input("¿Cuál es tu síntoma o consulta?")

if user_input:
    with st.spinner("Pensando..."):
        mensajes = [
            {"role": "system", "content": "Eres un asistente médico virtual amable y responsable. No das diagnósticos definitivos y siempre recomiendas visitar a un médico si es grave."},
            {"role": "user", "content": user_input}
        ]
        respuesta = openai.chat.completions.create(
            model=modelo,
            messages=mensajes,
            max_tokens=500
        )
        st.success(respuesta.choices[0].message.content.strip())