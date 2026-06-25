import json
from pathlib import Path

from .chunker import chunk_text

BASE_DIR = Path(__file__).resolve().parents[2]

with open(
    BASE_DIR / "output" / "dataset.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

chunked_data = []

for item in data:

    chunks = chunk_text(item["chapter_text"])

    for i, chunk in enumerate(chunks):

        chunked_data.append({
            "doc_id": f"{item['book_id']}_{item['chapter_id']}_{i}",

            "book_id": item["book_id"],
            "chapter_id": item["chapter_id"],
            "chunk_id": i,

            "chapter_title": item["chapter_title"],
            "chunk_text": chunk
        })

output_path = BASE_DIR / "output" / "chunked_dataset.json"

with open(
    output_path,
    "w",
    encoding="utf-8"
) as f:
    json.dump(chunked_data, f, ensure_ascii=False, indent=2)

print(f"Chunking DONE ✅")
print(f"Total Chunks: {len(chunked_data)}")