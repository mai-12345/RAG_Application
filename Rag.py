
import streamlit as st
import os
import numpy as np
import faiss #facebook AI Similarity search
from langchain.document_loaders import PyPDFLoader
import google.generativeai as genai
import tempfile
from sentence_transformers import SentenceTransformer

api = 'AIzaSyCPe0Qz3OXlJfP-BIzEv6v8iSGRIJ55RNc'

st.title('RAG Application Using Gemini AI')

#configure google generative AI
if api:
    genai.configure(api_key = api)
else:
    st.error('Your API Key is Not Found.')

def generate_text(text):
    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    response = model.generate_content(text)
    return response.text

if 'message' not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


#upload pdf file
upload_file = st.file_uploader('Choose File...', type = ['pdf'])

if upload_file is not None:
    with tempfile.NamedTemporaryFile(delete= False, suffix= '.pdf') as tempfile:
        tempfile.write(upload_file.read())
        tempfile_path = tempfile.name

    loader = PyPDFLoader(tempfile_path)
    documents = loader.load()
    #st.write(documents)

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    #create embedding
    text = [doc.page_content for doc in documents]
    embeddings = embedding_model.encode(text, show_progress_bar = True)
    embedding_matrix = np.array(embeddings)

    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)
    st.success('PDF Processed Successfuly.')

    user_input = st.chat_input('Please enter a text to search...')

    if user_input:
        with st.chat_message('user'):
            st.markdown(user_input)

        st.session_state.message.append({'role' : 'user', 'content': user_input})

        question_embedding = embedding_model.encode([user_input])

        k = 1
        distances, indices = index.search(question_embedding, k)
        similar_doc = [documents[i] for i in indices[0]]

        context = ""

        for i, doc in enumerate(similar_doc):
            context += doc.page_content + '\n'

        prompt = f'You are an assistant who retrieves answer based on the following content:{context}\n\nQuestion:{user_input}'
        response_text = generate_text(prompt)

        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            with st.spinner('Generating Answer'):
                response_text = generate_text(prompt)
                message_placeholder.markdown(f'{response_text}')
        st.session_state.message.append({'role' : 'assistant', 'content' : response_text})

else:
    st.write('Please Upload a PDF File.')






