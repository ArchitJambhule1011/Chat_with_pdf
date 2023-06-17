from PyPDF2 import PdfReader

def process_pdf(pdf):
    pdf_reader = PdfReader(pdf)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text