import streamlit as st
import tempfile
from PyPDF2 import PdfReader
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.document_loaders import UnstructuredWordDocumentLoader
from langchain.document_loaders import DirectoryLoader
from langchain.chains.conversation.memory import ConversationBufferWindowMemory,ConversationBufferMemory
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
import os
from langchain.llms import OpenAI
import openai
from dotenv import load_dotenv
from langchain.llms import Cohere
from langchain.embeddings.cohere import CohereEmbeddings
import cohere
import openai
from langchain.prompts.prompt import PromptTemplate
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()
 

 

# initialise API key.
api_key = os.getenv("COHERE_API_KEY")
user_api_key = api_key

 

# Upload file .

# documents=[]
# folder_path=r"C:\Users\2068357\PROMPT ENGINEERING\prompt engg nlp\regulatory complaince dummy data"
# loader = DirectoryLoader(folder_path, glob="*.docx", loader_cls=UnstructuredWordDocumentLoader)
# documents = loader.load()
# documents.extend(loader.load())

# Tokenization.

tokenizer = tiktoken.get_encoding('cl100k_base')
tiktoken.encoding_for_model('gpt-3.5-turbo')
def tiktoken_len(text):
    tokens=tokenizer.encode(
    text,
    disallowed_special=()
    )
    return len(tokens)

# token_counts=[tiktoken_len(doc.page_content) for doc in documents]
#   /////////////////////////
# PDF chat

st.header("chat with PDF")

# upload a PDF file.
pdf = st.file_uploader("Upload your PDF ",type='pdf')

if pdf is not None:
    pdf_reader = PdfReader(pdf)

    text =""
    for page in pdf_reader.pages:
        text+=page.extract_text()

#Chunking data.

        text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=['\n\n','\n',' ','']
        )       

 

        chunks=text_splitter.split_text(text=text)
# print(f'length of data is  {len(documents)}')

# Vector Embedding.
# embeddings = OpenAIEmbeddings()# default text davinchi .1
        model_name = "sentence-transformers/all-mpnet-base-v2"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        vectorstore = FAISS.from_texts(chunks, embeddings)

                # Initialise llm.

        llm = Cohere(
            temperature=0.0,
            model="command",
            cohere_api_key=user_api_key)


        template = """ Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
                    Context :
                    {context}
                    Question: {question}
                    Helpful Answer:

        """
        prompt = PromptTemplate(
            input_variables=["context","question"],
            template=template

        )


        #Initialise Memory

        memory = ConversationBufferWindowMemory(
            llm=llm,
            k=10,
            # output_key='answer',
            memory_key='chat_history',
            return_messages=True)

        

        # Initialise retriever
        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 15, "include_metadata": True})

        

        # Conversation Retrival Chain.
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            memory=memory,
            combine_docs_chain_kwargs={"prompt": prompt},
            chain_type="stuff",
            retriever=retriever,
            verbose=True)

 



 

#Conversation_chat code.


# def conversational_chat(query):
#     st.session_state['history'].append(query,result["answer"])



def conversational_chat(query):
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]
if 'history' not in st.session_state:
        st.session_state['history'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello ! Ask me anything from word file provided"]
if 'past' not in st.session_state:
    st.session_state['past'] = ["How may I help you?"]

#container for the chat history

response_container = st.container()
#container for the user's text input
container = st.container()
with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk about your dataset here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
        if submit_button and user_input:
            output = conversational_chat(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")