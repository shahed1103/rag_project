import os
import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

TFIDF_MATRIX_PATH = os.path.join(BASE_DIR, "output", "tfidf", "tfidf_matrix.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "output", "tfidf", "tfidf_vectorizer.pkl")
METADATA_PATH = os.path.join(BASE_DIR, "output", "tfidf", "tfidf_metadata.json")


def load_data():
    with open(TFIDF_MATRIX_PATH, "rb") as f:
        tfidf_matrix = pickle.load(f)

    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return tfidf_matrix, vectorizer, metadata


def search(query, tfidf_matrix, vectorizer, top_k=5):
    query_vec = vectorizer.transform([query])

    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    top_indices = scores.argsort()[::-1][:top_k]

    return top_indices, scores


if __name__ == "__main__":

    query = "ما هو الفقه"

    tfidf_matrix, vectorizer, metadata = load_data()

    idxs, scores = search(query, tfidf_matrix, vectorizer)

    print("Top Results (TF-IDF):")

    for i in idxs:
        print(i, scores[i])