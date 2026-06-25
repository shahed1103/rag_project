import json
from pathlib import Path

from .docx_utils import extract_docx_text
from .text_cleaner import clean_text

BASE_DIR = Path(__file__).resolve().parents[2]

books_folder = BASE_DIR / "data" / "Books"

with open(
   BASE_DIR / "data" / "metadata" / "chapters_metadata.json",
    "r",
    encoding="utf-8"
) as f:
    metadata = json.load(f)

dataset = []

if not books_folder.exists():
    raise FileNotFoundError(f"Books folder not found: {books_folder}")

for book_folder in sorted(books_folder.iterdir()):

    if not book_folder.is_dir():
        continue

    book_id = book_folder.name

    docx_files = sorted(book_folder.glob("Chapter*.docx"))

    for docx_file in docx_files:

        chapter_id = docx_file.stem

        chapter_meta = metadata.get(book_id, {}).get(chapter_id, {})

        chapter_text = extract_docx_text(docx_file)


        chapter_record = {
            "book_id": book_id,

            "chapter_id": chapter_id,

            "chapter_title": chapter_meta.get("chapter_title", ""),

            "chapter_text": clean_text(chapter_text),

            "video_youtube_url": chapter_meta.get("youtube_url", ""),
        }

        dataset.append(chapter_record)

output_path = BASE_DIR / "output" / "dataset.json"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Dataset size: {len(dataset)} chapters")
print(f"Saved to: {output_path}")