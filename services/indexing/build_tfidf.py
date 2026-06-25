import json
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "output", "chunked_dataset.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "tfidf")

TFIDF_MATRIX_PATH = os.path.join(OUTPUT_DIR, "tfidf_matrix.pkl")
VECTORIZER_PATH = os.path.join(OUTPUT_DIR, "tfidf_vectorizer.pkl")
METADATA_PATH = os.path.join(OUTPUT_DIR, "tfidf_metadata.json")


def load_chunks():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_tfidf():
    chunks = load_chunks()

    texts = [c["chunk_text"] for c in chunks]

    vectorizer = TfidfVectorizer(
    max_features=15000,
    ngram_range=(1,2),
    min_df=2,
    max_df=0.9,
    sublinear_tf=True,
    norm="l2",
    smooth_idf=True
    )
    

    tfidf_matrix = vectorizer.fit_transform(texts)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # save matrix
    with open(TFIDF_MATRIX_PATH, "wb") as f:
        pickle.dump(tfidf_matrix, f)

    # save vectorizer
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    # save metadata
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

    print("✅ TF-IDF BUILD DONE")
    print("Docs:", len(texts))
    print("Vocab size:", len(vectorizer.vocabulary_))


if __name__ == "__main__":
    build_tfidf()