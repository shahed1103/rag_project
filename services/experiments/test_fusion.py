from services.retrieval.fusion_search import fusion_search

query = "قصة اسلام عمر بن الخطاب"

results = fusion_search(query)

for i, result in enumerate(results, start=1):

    print(f"\n===== RESULT {i} =====")

    print("Score:")
    print(result["score"])

    print("Doc:")
    print(result["chunk_id"])

    print("Chapter:")
    print(result["chapter_title"])

    print("\nText:")
    print(result["text"][:500])