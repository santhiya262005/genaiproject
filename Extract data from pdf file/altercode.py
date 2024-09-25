import fitz  # PyMuPDF

# Open the PDF file
pdf_document = "path/to/your/pdf/file.pdf"
pdf = fitz.open(pdf_document)

# Iterate through each page
for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    text = page.get_text("text")
    print(f"Page {page_num + 1}:\n{text}\n")
