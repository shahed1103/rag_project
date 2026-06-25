from services.retrieval.query_processor import process_query

query = "ما معنى الثبات ، في حياة المسلم؟"

result = process_query(query)

print("\nProcessed Query:")
print(result["clean_query"])

print("\nTokens:")
print(result["tokens"])