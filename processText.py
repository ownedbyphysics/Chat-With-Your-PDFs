import os
import shutil
from PyPDF2 import PdfReader
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

openai_api_key = ''
CHROMA_PATH = "chroma"
DATA_PATH = "data/philosophy"

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
    #embeddings = openaiEmbeddings(OPEN_API_KEY=OPEN_API_KEY)
    vector_store = FAISS.from_texts(texts=chunks,
                                    embedding=embeddings)
    
    return vector_store


def chromaDB(chunks):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
    
