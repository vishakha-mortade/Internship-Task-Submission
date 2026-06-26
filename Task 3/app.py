
import warnings
warnings.filterwarnings("ignore")
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

 
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
 
try:
    from streamlit_mic_recorder import speech_to_text
    HAS_MIC = True
except ImportError:
    HAS_MIC = False

try:
    from utils import export_to_pdf
    HAS_PDF = True
except ImportError:
    HAS_PDF = False


 
@st.cache_data
def load_data():
    try:
        return pd.read_csv("medquad_clean.csv")
    except Exception:
        return pd.DataFrame(columns=['question', 'answer'])

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def get_corpus_embeddings(_model, text_list):
    # This caches the massive math calculation so it only runs ONCE!
    return _model.encode(text_list, convert_to_tensor=True)


 
def log_unanswered_query(query):
    """Saves queries that fell below the 0.4 similarity threshold."""
    with open("unanswered_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User asked: {query}\n")

SAFETY_RULES = {
    "diabetes": ["sugar", "glucose", "carbohydrates", "insulin", "sweetener", "diabetic"],
    "hypertension": ["salt", "sodium", "caffeine", "exercise", "stress", "blood pressure"],
    "asthma": ["smoke", "dust", "pollen", "inhaler", "breathing", "lung"],
    "allergy": ["penicillin", "antibiotic", "latex", "nuts", "shellfish"]
}

def apply_safety_filter(answer, history):
    if not history: 
        return []
        
    history_lower = history.lower()
    answer_lower = answer.lower()
    active_warnings = []
    
    for condition, triggers in SAFETY_RULES.items():
        if condition in history_lower:
            for word in triggers:
                if word in answer_lower:
                    active_warnings.append(f"⚠️ **{condition.upper()} NOTICE:** This response mentions '{word}'. Please verify with your doctor.")
                    break # Stop checking this condition once we find a trigger
                    
    return active_warnings


def main():
    st.set_page_config(page_title="MediQuery AI", page_icon="🩺", layout="wide")

    
    with st.sidebar:
        st.title("📋 Patient Profile")
        st.markdown("Configure your profile for safety checks.")
        
        chronic_condition = st.selectbox(
            "Chronic History",
            ["None", "Diabetes", "Hypertension", "Asthma"]
        )
        known_allergies = st.text_input("Known Allergies (optional)")
        user_history = f"{chronic_condition} {known_allergies}"
        
        st.markdown("---")
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            st.rerun()

        if HAS_PDF:
            st.markdown("---")
            if "messages" in st.session_state and len(st.session_state.messages) > 0:
                try:
                    pdf_data = export_to_pdf(st.session_state.messages)
                    st.download_button("📥 Download Summary PDF", pdf_data, "MediQuery_Report.pdf")
                except Exception:
                    pass

        st.markdown("---")
        st.info("⚖️ **Ethical Disclaimer:**\nThis system is a prototype using the NIH MedQuAD dataset adapted for the Indian context. It is for educational purposes only.")

    
    st.title("🩺 MediQuery: Advanced Medical Assistant")
    st.caption("Hybrid RAG System (Semantic Search) with Safety Guardrails")

    df = load_data()
    if df.empty:
        st.error("Database not found! Please ensure 'medquad_clean.csv' is in the project folder.")
        return

    model = load_model()
    
    with st.spinner("Initializing Vector Database (This may take a minute on the very first run...)"):
        corpus_embeddings = get_corpus_embeddings(model, df['question'].tolist())

    if "messages" not in st.session_state:
        st.session_state.messages = []

    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

   
    v_input = None
    if HAS_MIC:
        st.write("### ⏺️ Voice Search")
        v_input = speech_to_text(language='en-IN', start_prompt="Click to speak your symptoms", key='STT')

    user_query = st.chat_input("Type a medical question here...")
    
    if v_input: 
        user_query = v_input
 
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            with st.spinner("Searching medical knowledge base..."):
                raw_answer = None
                
                
                keyword_match = df[df['question'].str.contains(user_query, case=False, na=False)]
                
                if not keyword_match.empty:
                    raw_answer = keyword_match.iloc[0]['answer']
                else:
                    
                    query_emb = model.encode(user_query, convert_to_tensor=True)
                    scores = util.cos_sim(query_emb, corpus_embeddings)[0]
                    best_idx = torch.argmax(scores).item()
                    
                  
                    if scores[best_idx] > 0.4:
                        raw_answer = df.iloc[best_idx]['answer']
                    else:
                        raw_answer = "I'm sorry, I couldn't find a safe, verified match in my dataset for that question."
                        log_unanswered_query(user_query)
 
                if raw_answer and "I'm sorry" not in raw_answer:
                    raw_answer = raw_answer.replace("9-1-1", "**102 (Ambulance) / 108 (Emergency)**")
                    raw_answer = raw_answer.replace("911", "**102 (Ambulance) / 108 (Emergency)**")
                    raw_answer = raw_answer.replace("poison control center", "**National Poisons Information Centre (1800-116-117)**")
                    raw_answer = raw_answer.replace("1-800-222-1222", "**1800-116-117**")

         
                personal_warnings = apply_safety_filter(raw_answer, user_history)
                
                if personal_warnings:
                    for warn in personal_warnings:
                        st.error(warn) 
                
                st.markdown(raw_answer)
                st.session_state.messages.append({"role": "assistant", "content": raw_answer})

if __name__ == "__main__":
    main()