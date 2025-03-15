from pathlib import Path
from docling.document_converter import DocumentConverter

if __name__ == "__main__":
    input_doc_path = Path("./tests/data/pdf/BRI-STATEMENT.pdf")
    output_dir = Path("./output/data/csv")

    doc_converter = DocumentConverter()
    conv_res = doc_converter.convert(input_doc_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    doc_filename = conv_res.input.file.stem

    for table_ix, table in enumerate(conv_res.document.tables):
        table_df = table.export_to_dataframe()
        element_csv_filename = output_dir / f"{doc_filename}-table-{table_ix+1}.csv"
        table_df.to_csv(element_csv_filename, index=False)