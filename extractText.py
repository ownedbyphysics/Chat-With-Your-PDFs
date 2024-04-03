from PyPDF2 import PdfReader

def extractPdfText(documents):
    text=""
    for pdf in documents:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text = text + page.extract_text()
            
    return text