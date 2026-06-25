from services.retrieval.query_processor import process_query
from services.retrieval.query_embedding import build_query_embedding

query = "ما معنى الثبات في حياة المسلم؟"

processed = process_query(query)

embedding = build_query_embedding(
    processed["clean_query"]
)

print("Shape:")
print(embedding.shape)

print("\nFirst 10 values:")
print(embedding[:10])