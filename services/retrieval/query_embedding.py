from sentence_transformers import SentenceTransformer
from services.retrieval.query_processor import process_query

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

print("Loading embedding model...")
model = SentenceTransformer(MODEL_NAME)


def build_query_embedding(query: str):
    """
    Convert query into embedding vector.
    """

    processed = process_query(query)
    clean = processed["clean_query"]

    # الأفضل لهذا الموديل: بدون artificial prompt
    return model.encode(
        clean,
        normalize_embeddings=True
    )