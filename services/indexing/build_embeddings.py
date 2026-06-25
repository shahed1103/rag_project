import json
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "output", "chunked_dataset.json")

OUTPUT_DIR = os.path.join(BASE_DIR, "output", "embeddings")

EMBEDDINGS_PATH = os.path.join(OUTPUT_DIR, "embeddings.npy")

METADATA_PATH = os.path.join(OUTPUT_DIR, "embeddings_metadata.json")

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

def load_chunks():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_embeddings():
    chunks = load_chunks()

    texts = [c["chunk_text"] for c in chunks]

    print("Loading model... (this may take time first run)")

    model = SentenceTransformer(MODEL_NAME)

    embedding_dim = model.get_sentence_embedding_dimension()
    print("Encoding documents...")

    embeddings = model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    np.save(EMBEDDINGS_PATH, embeddings)

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

    print("✅ EMBEDDINGS BUILD DONE")
    print("Docs:", len(texts))
    print("Embedding dim:", embeddings.shape)


if __name__ == "__main__":
    build_embeddings()