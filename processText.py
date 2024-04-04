from PyPDF2 import PdfReader
from langchain_community.vectorstores import FAISS
#from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter


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


def textChunks(text):
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


def vectorDB(chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = openaiEmbeddings(OPEN_API_KEY=OPEN_API_KEY)
    vector_store = FAISS.from_texts(texts=chunks,
                                    embedding=embeddings)
    
    return vector_store