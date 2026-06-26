import os
import sys
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

GOOGLE_API_KEY = "MY_API_KEY"
DB_PATH = "./chroma_db_storage"

def initialize_rag_pipeline():
    if not os.path.exists(DB_PATH):
        print(f"Error: Vector store not found at {DB_PATH}. Please run Update_knowledge.py.")
        sys.exit(1)

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest", 
        google_api_key=GOOGLE_API_KEY, 
        temperature=0.1,
        disable_streaming=True
    )
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004", 
        google_api_key=GOOGLE_API_KEY
    )
    
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question based strictly on the context provided below. 
    If the answer is not in the context, state that you do not have the information.
    
    Context:
    {context}
    
    Question: 
    {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, document_chain)

def chat_interface():
    retrieval_chain = initialize_rag_pipeline()
    print("Bot initialized. Type 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                break
                
            response = retrieval_chain.invoke({"input": user_input})
            print(f"Bot: {response['answer']}\n")
            
        except Exception as e:
            print(f"Runtime Error: {e}\n")

if __name__ == "__main__":
    chat_interface()