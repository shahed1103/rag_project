from docx import Document


def extract_docx_text(docx_path):
    doc = Document(docx_path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)