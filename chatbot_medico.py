import os
from openai import OpenAI

# Autenticación (pon tu API key aquí)
client = OpenAI(api_key="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")

# Función del chatbot
def responder_chat(mensaje_usuario):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "Eres un asistente médico que responde de forma clara, responsable y respetuosa. No haces diagnósticos, solo orientas al paciente."},
            {"role": "user", "content": mensaje_usuario}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

# Ejemplo de uso
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "exit", "quit"]:
        break
    respuesta = responder_chat(entrada)
    print("Asistente médico:", respuesta)