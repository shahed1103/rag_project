from services.retrieval.bm25_search import search_bm25

query = "قصة اسلام عمر بن الخطاب"

results = search_bm25(
    query,
    top_k=5
)


for i, result in enumerate(results, 1):

    print(f"\n===== RESULT {i} =====")

    print(f"Score: {result['score']}")
    print(f"doc_id: {result['chunk_id']}")
    print(f"Book: {result['book_id']}")
    print(f"Chapter: {result['chapter_title']}")

    # print("\nTEXT:")
    print(result["text"][:400])