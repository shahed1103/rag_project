# services/experiments/test_query_tfidf.py

from services.retrieval.query_processor import process_query
from services.retrieval.query_tfidf import build_query_tfidf

query = "ما معنى الثبات في حياة المسلم؟"

processed = process_query(query)

query_vector = build_query_tfidf(
    processed["clean_query"]
)

print("Shape:")
print(query_vector.shape)

print("Non Zero Features:")
print(query_vector.nnz)