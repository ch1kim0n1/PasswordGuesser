import PyPDF2
import os

pdf_file = r"FILE/PATH/HERE"

# Verify PDF file exists
if not os.path.isfile(pdf_file):
    print(f"File not found: {pdf_file}")
    exit()
else:
    print(f"File found: {pdf_file}")