import streamlit as st
import fitz 
import tempfile
from io import BytesIO

def extract_text_from_pdf(file):
    pdf_text = ""
    if file is not None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = f"{temp_dir}/uploaded_file.pdf"

            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(file.read())

            with fitz.open(temp_file_path) as pdf_document:
                for page_number in range(len(pdf_document)):
                    page = pdf_document[page_number]
                    pdf_text += page.get_text()

    return pdf_text

st.title("PDF Text Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    pdf_contents = extract_text_from_pdf(uploaded_file)
    st.header("PDF Contents:")
    st.text(pdf_contents)