from src.process_pdf import process_pdf
from src.split_text import split_text
from src.create_vector_base import create_vector_base
from src.run_question_answering import run_question_answering
from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader



def main():
    load_dotenv()
    st.set_page_config(page_title='Question your pdf')
    st.header('Chat with your pdf')

    pdf = st.file_uploader('Upload your pdf', type='pdf')

    if pdf is not None:
        text = process_pdf(pdf)
        chunks = split_text(text)
        vector_base = create_vector_base(chunks)

        user_q = st.text_input('Ask your question')
        if user_q:
            response = run_question_answering(user_q, vector_base)
            st.write(response)

if __name__ == '__main__':
    main()