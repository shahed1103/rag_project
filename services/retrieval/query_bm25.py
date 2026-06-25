# services/retrieval/query_bm25.py

from services.retrieval.query_processor import process_query


def build_query_bm25(query: str):
    processed = process_query(query)
    """
    BM25 representation of query.
    For BM25 the representation is simply the tokenized query.
    """
    tokens = processed["tokens"]

    return tokens