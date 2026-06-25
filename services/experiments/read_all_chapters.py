from pathlib import Path
from pdf_utils import extract_pdf_text

book_folder = Path("../data/Books/Book1")

# for pdf_file in book_folder.glob("*.pdf"):
#     text = extract_pdf_text(pdf_file)

for file in book_folder.iterdir():
    print(file.name)

    # print(f"\n{'=' * 50}")
    # print(f"File: {pdf_file.name}")
    # print(f"Characters: {len(text)}")