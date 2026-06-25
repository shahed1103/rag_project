from services.retrieval.query_processor import process_query
from services.retrieval.query_bm25 import build_query_bm25

query = "ما معنى الثبات في حياة المسلم؟"

processed = process_query(query)

bm25_query = build_query_bm25(
    processed["tokens"]
)

print("BM25 Query:")
print(bm25_query)