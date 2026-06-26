import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
 
GOOGLE_API_KEY = "MY_API_KEY" 
FOLDER_PATH = "./knowledge_source"
DB_PATH = "./chroma_db_storage"

def update_db():
    print(f"Checking {FOLDER_PATH} for new data...")

    if not os.path.exists(FOLDER_PATH):
        print(f"Error: Folder '{FOLDER_PATH}' does not exist. Please create it.")
        return

 
    loader = DirectoryLoader(FOLDER_PATH, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if not documents:
        print("No text files found to add.")
        return

     
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

     
    print("Updating database... this might take a moment.")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=GOOGLE_API_KEY)
    db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_PATH)
    
    print(f"Success! Added {len(chunks)} new chunks of information to the bot's memory.")

if __name__ == "__main__":
    update_db()