from services.retrieval.tfidf_search import search_tfidf

query = "قصة اسلام عمر بن الخطاب"

results = search_tfidf(
    query,
    top_k=5
)

for i, result in enumerate(results, start=1):

    print(f"\n================ RESULT {i} ================")

    # print(f"ID: {result['doc_id']}")
    print(f"Score: {result['score']:.4f}")
    print(f"doc_id: {result['chunk_id']}")
    print(f"Book: {result['book_id']}")
    print(f"Chapter: {result['chapter_title']}")

    # print("\nTEXT:")
    print(result["text"][:400])