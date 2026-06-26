import json
import pandas as pd

from services.evaluation.evaluate import (
    precision_at_k,
    recall_at_k,
    average_precision,
    ndcg
)

from services.retrieval.tfidf_search import search_tfidf
from services.retrieval.bm25_search import search_bm25
from services.retrieval.vector_search import search_qdrant
from services.retrieval.fusion_search import fusion_search


K = 10


# =========================
# Load Ground Truth
# =========================
def load_ground_truth(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# Evaluate one system
# =========================
def evaluate_system(ground_truth, search_fn, system_name):
    results = []

    for item in ground_truth:
        query = item["query"]
        relevant = item["relevant_docs"]

        retrieved_docs = search_fn(query)

        retrieved_ids = [r["chunk_id"] for r in retrieved_docs]

        p = precision_at_k(relevant, retrieved_ids, K)
        r = recall_at_k(relevant, retrieved_ids, K)
        ap = average_precision(relevant, retrieved_ids, K)
        n = ndcg(relevant, retrieved_ids, K)

        results.append((p, r, ap, n))

    # average
    avg_p = sum(x[0] for x in results) / len(results)
    avg_r = sum(x[1] for x in results) / len(results)
    avg_ap = sum(x[2] for x in results) / len(results)
    avg_ndcg = sum(x[3] for x in results) / len(results)

    return {
        "System": system_name,
        "Precision@10": avg_p,
        "Recall@10": avg_r,
        "MAP": avg_ap,
        "nDCG": avg_ndcg
    }


# =========================
# RUN ALL SYSTEMS
# =========================
def main():
    gt_path = "services/evaluation/ground_truth.json"
    ground_truth = load_ground_truth(gt_path)

    print(f"Evaluating on {len(ground_truth)} queries...\n")

    report = []

    report.append(evaluate_system(ground_truth, search_tfidf, "TF-IDF"))
    report.append(evaluate_system(ground_truth, search_bm25, "BM25"))
    report.append(evaluate_system(ground_truth, search_qdrant, "Embedding"))
    report.append(evaluate_system(ground_truth, fusion_search, "Fusion"))

    df = pd.DataFrame(report)

    print("\n===== FINAL RESULTS =====")
    print(df)

    df.to_csv("output/evaluation_results.csv", index=False)
    print("\nSaved to output/evaluation_results.csv")


if __name__ == "__main__":
    main()