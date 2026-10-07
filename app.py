import os

import pdfplumber
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import SecretStr


def get_api_key() -> str:
    try:
        key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        key = os.getenv("GEMINI_API_KEY")
    if not key:
        st.error(
            "Gemini API key not found. Add GEMINI_API_KEY to .streamlit/secrets.toml "
            "or set it as an environment variable."
        )
        st.stop()
    return key


GEMINI_API_KEY = get_api_key()

st.header("DocuMind")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract contents from the PDF and chunk it
if file is not None:
    # extract text from it
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    # st.write(text)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # generating embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=SecretStr(GEMINI_API_KEY)
    )

    # store embeddings in vector db
    vector_store = FAISS.from_texts(chunks, embeddings)

    # get user questions
    user_question = st.text_input("Type your question")

    # generate answer
    # question -> embedding -> similarity search -> results to LLM -> response (CHAIN)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
    )

    # define the llm and prompt
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=SecretStr(GEMINI_API_KEY),
        temperature=0.3,
        max_output_tokens=500
    )

    # provide the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistant answering questions about a PDF document. \n\n"
         "Guidelines:\n"
         "1. Provide complete, well-explained answers using the context below. \n"
         "2. Include relevant details, numbers and explanations to give a thorough response. \n"
         "3. If the context mentions related information, include it to give fuller picture. \n"
         "4. Only use information from the provided context - do not use outside knowledge. \n"
         "5. Summarize long information, ideally in bullets where needed. \n"
         "6. If the information is not in the context, say so politely. \n\n"
         "Context:\n{context}"),
        ("human", "{question}")
    ])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)