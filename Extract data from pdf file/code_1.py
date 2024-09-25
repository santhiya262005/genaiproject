from thepipe.extract import extract_from_file

# Define your schema
schema = {
    "fields": [
        {"name": "Item", "type": "string"},
        {"name": "Quantity", "type": "integer"},
        {"name": "Unit Price", "type": "float"},
        {"name": "Total Price", "type": "float"}
    ]
}

# Extract data from the PDF
results = extract_from_file(
    file_path="path/to/your/pdf/file.pdf",
    schema=schema,
    ai_model="google/gemini-flash-1.5b",
    chunking_method="chunk_by_page"
)

# Print the results
print(results)
