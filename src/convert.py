import pandas as pd
from io import BytesIO
from typing import Iterator
from docling_core.types.io import DocumentStream
from docling.document_converter import DocumentConverter

def convert_pdf_to_dataframe(stream: BytesIO) -> Iterator[pd.DataFrame]:
    source = DocumentStream(name="document.pdf", stream=stream)
    doc_converter = DocumentConverter()
    conv_res = doc_converter.convert(source)

    for table in conv_res.document.tables:
        yield table.export_to_dataframe()