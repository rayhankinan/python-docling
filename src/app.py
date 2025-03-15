import pandas as pd
from io import BytesIO
from typing import Iterator
import streamlit as st
from docling_core.types.io import DocumentStream
from docling.document_converter import DocumentConverter

def convert_pdf_to_dataframe(stream: BytesIO) -> Iterator[pd.DataFrame]:
    source = DocumentStream(name="document.pdf", stream=stream)
    doc_converter = DocumentConverter()
    conv_res = doc_converter.convert(source)

    for table in conv_res.document.tables:
        yield table.export_to_dataframe()

def main() -> None:
    st.title("PDF to CSV Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is None:
        return

    converting = st.empty()

    if converting.button("Convert PDF to CSV", disabled=False, key="convert_button1"):
        converting.button("Converting...", disabled=True, key="convert_button2")

        for i, df in enumerate(convert_pdf_to_dataframe(uploaded_file)):
            try:
                st.subheader(f"Table {i+1}")
                st.dataframe(df)

            except Exception as e:
                st.error(f"An error occurred: {e}")

        converting.button("Convert PDF to CSV", disabled=False, key="convert_button3")

if __name__ == "__main__":
    main()