# RAG Application Using Gemini AI

## 📌 Project Description
This project implements a **Retrieval-Augmented Generation (RAG)** system using Google's **Gemini AI**. It allows users to upload a PDF file, process its content, and retrieve relevant information based on user queries. The system leverages **FAISS** for similarity search and **Sentence Transformers** for text embeddings.

## 🛠️ Requirements
Before running the project, ensure you have the following dependencies installed:

```bash
pip install streamlit faiss-cpu langchain google-generativeai sentence-transformers pypdf numpy
```

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/rag-gemini
   cd rag-gemini
   ```
2. Install the required dependencies using the command above.
3. Run the Streamlit application:
   ```bash
   streamlit run Rag.py
   ```
4. Upload a PDF file and enter a query to retrieve relevant information.

## 🏗️ Project Structure
```
📂 RAG-Gemini
├── 📄 Rag.py          # Main application script
├── 📄 README.md       # Project documentation
└── 📄 requirements.txt # Dependencies list
```

## 📌 Features
✅ Upload and process a PDF document  
✅ Extract embeddings using Sentence Transformers  
✅ Perform similarity search with FAISS  
✅ Generate responses using **Gemini AI**  

## 🔥 Example Usage
- **User Input:** "What are the key points in the document?"
- **Generated Response:** "The document highlights the main points including..."

## 🛡️ API Key Configuration
The application requires a **Google Gemini AI API Key**. Make sure to set your API key correctly inside the `Rag.py` script:
```python
api = 'YOUR_GOOGLE_GEMINI_API_KEY'
```



