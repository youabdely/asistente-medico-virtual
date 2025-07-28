# 🩺 Asistente Médico Virtual

Este proyecto consiste en un chatbot de atención médica básica desarrollado en Python, utilizando **Streamlit** para la interfaz web y **OpenAI GPT** como motor de inteligencia artificial.

---
git
## 📌 Objetivo

El objetivo de este asistente es ofrecer respuestas rápidas a consultas médicas generales y orientar al usuario sobre cuándo debe acudir a un profesional sanitario, **sin reemplazar en ningún momento una consulta médica real**.

---

## ⚙️ Tecnologías utilizadas

- 🐍 **Python 3.10+**
- 🤖 **OpenAI GPT** (modelo `gpt-3.5-turbo` o `gpt-4`)
- 🌐 **Streamlit**
- 🗂️ **Git & GitHub**

---

## 🚀 ¿Cómo ejecutarlo localmente?

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/asistente-medico.git
cd asistente-medico
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Añadir la clave de API de OpenAI

En sistemas **Linux/macOS**:

```bash
export OPENAI_API_KEY="tu_clave_aqui"
```

En **Windows (CMD)**:

```cmd
set OPENAI_API_KEY=tu_clave_aqui
```

> 🔐 Asegúrate de tener una clave válida de OpenAI y no compartirla públicamente.

### 4. Ejecutar la aplicación

```bash
streamlit run asistente_web.py
```

---

## 📎 Notas adicionales

- Este chatbot **no proporciona diagnósticos médicos reales**.
- Es una herramienta de apoyo educativo y de orientación inicial.
- Se recomienda su uso como ejemplo de aplicación de IA en salud, no como producto clínico final.