from services.llm.gemini_client import ask_gemini

answer = ask_gemini(
    "ما هو تعريف التوازن؟"
)

print(answer)