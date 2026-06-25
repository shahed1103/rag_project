from pdf_utils import extract_pdf_text
from text_cleaner import clean_text

text = extract_pdf_text(
    "../data/Books/Book1/Chapter1.pdf"
)

cleaned_text = clean_text(text)

print(cleaned_text[:5000])