from services.rag.rag_pipeline import ask

result = ask(
    "ما هو تعريف التوازن"
)

print(result["answer"])