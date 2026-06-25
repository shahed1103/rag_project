from services.retrieval.hybrid_search import hybrid_search

query = "ما معنى التوازن؟"

results = hybrid_search(query)

for i, r in enumerate(results, 1):

    print(f"\n===== RESULT {i} =====")
    print("Score:", r["score"])
    print("Book:", r["chunk"]["doc_id"])
    print("Book:", r["chunk"]["book_id"])
    print("Chapter:", r["chunk"]["chapter_id"])
    print("Chapter Title:", r["chunk"]["chapter_title"])
    # print("Text:", r["chunk"]["chunk_text"][:300])