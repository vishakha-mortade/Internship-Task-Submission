# Project Overview

The goal of this project was to build a chatbot that doesn't just read static text, but can actually update its own knowledge, look at images, understand user emotions, search academic and medical databases, and speak multiple languages naturally.

###  The 6 Core Features

1. Dynamic Knowledge Base (FAISS + RAG)
     What it does: he chatbot automatically reads new `.txt` files added to a local folder and updates its brain without needing to be restarted.
     How: Uses LangChain and FAISS for incremental vector database updates.

2. Multi-Modal Vision Engine
     What it does: You can upload images alongside your text questions. 
     How: Uses Google Gemini 1.5 Flash and the PIL library to analyze pixels and text together.

3. Specialized Medical Assistant
     What it does: Safely answers health-related questions using the verified MedQuAD clinical dataset.
     How: Searches a custom FAISS index and uses strict system prompts to prevent AI hallucinations (includes a medical disclaimer).

4. ArXiv Domain Expert
    What it does: Acts as a research assistant. It can instantly search through 10,000+ Computer Science and Machine Learning abstracts.
    How:Pre-computed FAISS vector index loaded into Streamlit's server memory (`@st.cache_resource`) for lightning-fast academic retrieval.

5. Emotionally Intelligent Responses
     What it does: Reads the user's mood and changes its tone. If you are frustrated, it apologizes and gets straight to the point.
     How: Uses `TextBlob` to calculate sentiment polarity in real-time and dynamically injects instructions into the LLM prompt.

6. Native Multilingual Support
     What it does: Automatically detects the language you are typing in (English, Hindi, Marathi, Spanish, Hinglish) and replies in that exact language script.
     How: Uses Gemini's native localization capabilities rather than relying on clunky third-party translation APIs.

##  Tech Stack

 Language: Python 3.10+
 Frontend UI: Streamlit
 AI Models: Google Gemini Pro & Gemini 1.5 Flash (via `google-generativeai`)
 Vector Database: FAISS (Facebook AI Similarity Search)
 Orchestration & NLP: LangChain, TextBlob
 Data Handling: Pandas, PIL (Pillow)

##  How to Run This Project Locally

If you want to test this out on your own machine, follow these steps:

1. Clone the repository
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
