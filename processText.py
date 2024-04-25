import os
import shutil
from PyPDF2 import PdfReader
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

openai_api_key = ''

def extractPdfText(documents):
    """
    Extracts raw text from the pdfs
    """
    text=""
    for pdf in documents:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text = text + page.extract_text()
            
    return text


def textChunks_old(text):
    """
    Splits the extracted text to chunks
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks


def textChunks(text, save):
    """
    Splits the extracted text to chunks
    """
    if not save:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks = text_splitter.split_text(text)
        
    else:
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
        chunks = text_splitter.create_documents([text])
        
    return chunks


def vectorDB(chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_store = FAISS.from_texts(texts=chunks,
                                    embedding=embeddings)
    
    return vector_store


def chromaDB(chunks, name):

    try:
        db = Chroma.from_documents(
        documents=chunks, 
        embedding= OpenAIEmbeddings(openai_api_key=openai_api_key),
        persist_directory=name
        )
        db.persist()
        return 'your ' +  name + ' dabase has been created'
    except:
        return 'failed'

    
def retriever(database_name):
    vectordb = Chroma(persist_directory=str(database_name), 
                      embedding_function=OpenAIEmbeddings(openai_api_key=openai_api_key))

    retriever = vectordb.as_retriever()

    return retriever