import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PyPDF2 import PdfReader

load_dotenv()
GEMINI_API_KEY = os.getenv("API_KEY")
if not GEMINI_API_KEY:
    st.error("Clé API Gemini non trouvée.")
    st.stop()
genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("models/gemini-2.5-pro")
except Exception as e:
    st.error(f"Erreur lors de l'initialisation du modèle : {e}")
    st.stop()

st.set_page_config(page_title="Chatbot Gemini Doc", layout="wide")
st.title("Chatbot Gemini avec documents")
st.markdown("Posez une question ou chargez un document texte / PDF.")

if "history" not in st.session_state:
    st.session_state.history = []
if "docs" not in st.session_state:
    st.session_state.docs = ""

def extract_text_from_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return ""

with st.sidebar:
    st.header("Documents")
    uploaded_files = st.file_uploader("Importer .txt ou .pdf", type=["txt", "pdf"], accept_multiple_files=True)
    if uploaded_files:
        st.session_state.docs = ""
        for file in uploaded_files:
            text = extract_text_from_file(file)
            st.session_state.docs += f"\n--- {file.name} ---\n{text}"
        st.success("Documents chargés")

    if st.button("Réinitialiser tout"):
        st.session_state.history = []
        st.session_state.docs = ""
        st.experimental_rerun()

def chatbot_with_context(user_input):
    history = st.session_state.history[-10:]
    conversation = "\n".join([f"{role}: {msg}" for role, msg in history])
    prompt = f"""
Contexte documentaire :
{st.session_state.docs}

Historique de conversation :
{conversation}

Utilisateur: {user_input}
Gemini:"""
    response = model.generate_content(prompt)
    st.session_state.history.append(("Utilisateur", user_input))
    st.session_state.history.append(("Gemini", response.text))
    return response.text

user_input = st.text_input("Votre question", "")

if st.button("Envoyer") and user_input:
    with st.spinner("Gemini réfléchit..."):
        try:
            response = chatbot_with_context(user_input)
            st.markdown("### Réponse de Gemini")
            st.markdown(
                f"""
                <div style='background-color:#3b3f45; color:#f1f1f1;
                            padding:15px; border-radius:10px; margin-top:10px;
                            font-size: 1rem; line-height:1.5'>
                {response}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Erreur : {e}")

if st.session_state.history:
    st.subheader("Historique de la conversation (limité)")
    for role, message in st.session_state.history[::-1]:
        bg_color = "#2c2f35" if role == "Utilisateur" else "#3b3f45"
        text_color = "#f1f1f1"

        display_text = message.strip()
        if len(display_text) > 600:
            display_text = display_text[:600] + " [...]"

        st.markdown(f"""
        <div style='background-color:{bg_color}; color:{text_color}; 
                    padding:12px; border-radius:10px; margin-bottom:12px;
                    font-size: 0.9rem; line-height:1.4'>
        <b>{role} :</b><br>{display_text}
        </div>
        """, unsafe_allow_html=True)