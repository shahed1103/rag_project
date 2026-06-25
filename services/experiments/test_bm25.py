import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "output", "bm25", "bm25_model.pkl")


def search(query, top_k=5):
    with open(MODEL_PATH, "rb") as f:
        bm25 = pickle.load(f)

    tokens = query.split()

    scores = bm25.get_scores(tokens)

    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

    return top_indices, [scores[i] for i in top_indices]


if __name__ == "__main__":
    q = "ما هو الفقه"
    idxs, scores = search(q)

    print("Top Results:")
    for i, s in zip(idxs, scores):
        print(i, s)