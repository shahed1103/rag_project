import pickle
from pathlib import Path
from services.retrieval.query_processor import process_query

BASE_DIR = Path(__file__).resolve().parents[2]

with open(
    BASE_DIR / "output" / "tfidf" / "tfidf_vectorizer.pkl",
    "rb"
) as f:
    vectorizer = pickle.load(f)


def build_query_tfidf(query: str):

    processed = process_query(query)

    clean_query = processed["clean_query"]

    # safety check
    if not isinstance(clean_query, str):
        clean_query = " ".join(clean_query)

    return vectorizer.transform([clean_query])