from services.retrieval.fusion_search import fusion_search
from services.rag.prompt_builder import build_prompt

query = "ما هو تعريف التوازن"

chunks = fusion_search(query)

prompt = build_prompt(query, chunks)

print(prompt)