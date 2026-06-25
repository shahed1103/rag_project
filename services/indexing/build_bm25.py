import json
import os
import pickle
from rank_bm25 import BM25Okapi


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "output", "chunked_dataset.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "bm25")

BM25_MODEL_PATH = os.path.join(OUTPUT_DIR, "bm25_model.pkl")
METADATA_PATH = os.path.join(OUTPUT_DIR, "bm25_metadata.json")


def load_chunks():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def tokenize(text):
    return text.split()


def build_bm25():
    chunks = load_chunks()
    docs_count = len(chunks)

    corpus = (
        tokenize(c["chunk_text"]) 
        for c in chunks
    )

    bm25 = BM25Okapi(corpus, k1=1.5, b=0.75)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # حفظ النموذج
    with open(BM25_MODEL_PATH, "wb") as f:
        pickle.dump(bm25, f)

    # حفظ metadata
    metadata = [
        {
            "doc_id": c["doc_id"],
            "chunk_id": c["chunk_id"],
            "book_id": c["book_id"],
            "chapter_id": c["chapter_id"],
            "chapter_title": c["chapter_title"],
            "chunk_text": c["chunk_text"]
        }
        for c in chunks
    ]

    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print("✅ BM25 BUILD DONE")
    print("Docs:", docs_count)


if __name__ == "__main__":
    build_bm25()