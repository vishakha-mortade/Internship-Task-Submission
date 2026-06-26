import streamlit as st
import pandas as pd
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS

 
st.set_page_config(page_title="CS Expert Bot", layout="wide")

 
os.environ["GOOGLE_API_KEY"] = "xyascvbh" 

st.title(" ArXiv Computer Science Expert")
st.markdown("Ask me to explain complex CS concepts or summarize specific research.")
 
@st.cache_resource
def load_knowledge_base():
    if not os.path.exists('cs_papers.csv'):
        st.error("Please run process_data.py first!")
        return None, None

    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

     
    if os.path.exists("faiss_index"):
         
        vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    else:
        with st.spinner("Building NEW vector database (this uses 3072-dim embeddings)..."):
            df = pd.read_csv('cs_papers.csv')
            texts = (df['title'] + " " + df['abstract']).tolist()
            metadatas = [{"title": t} for t in df['title']]
            vector_db = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
          
            vector_db.save_local("faiss_index")
    
 
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    return vector_db, llm

 
try:
    vector_db, llm = load_knowledge_base()
except Exception as e:
    st.error(f"Failed to initialize: {e}")
    st.info("TIP: If you just changed your model, try deleting the 'faiss_index' folder manually.")
    st.stop()
 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

 
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

 
if user_query := st.chat_input("Explain the Transformer architecture..."):
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

     
    with st.chat_message("assistant"):
        with st.spinner("Analyzing research papers..."):
            # Search relevant chunks
            docs = vector_db.similarity_search(user_query, k=3)
            context = "\n\n".join([f"Paper: {d.metadata['title']}\nAbstract: {d.page_content}" for d in docs])
       
            expert_prompt = f"""
            You are a Computer Science Professor. Use the following research abstracts to answer the query.
            If the answer isn't in the context, use your general knowledge but mention it's general info.
            
            CONTEXT:
            {context}
            
            QUERY: {user_query}
            """
            
            response = llm.invoke(expert_prompt)
            st.markdown(response.content)
            
          
            with st.expander("View Source Papers"):
                for d in docs:
                    st.write(f"📍 **{d.metadata['title']}**")

    st.session_state.chat_history.append({"role": "assistant", "content": response.content})