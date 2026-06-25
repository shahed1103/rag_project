from docx_utils import extract_docx_text

text = extract_docx_text(
    "../data/Books/Book1/Chapter1_Exam1.docx"
)

print(text[:1000])