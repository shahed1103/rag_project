import json

# تحميل البيانات المقطعة
with open("output/chunked_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total chunks:", len(data))

# 1. متوسط حجم الـ chunks
sizes = [len(x["chunk_text"].split()) for x in data]

chunk0_words = data[0]["chunk_text"].split()
chunk1_words = data[1]["chunk_text"].split()

print("Last 60 words of chunk0:")
print(" ".join(chunk0_words[-60:]))

print("\nFirst 60 words of chunk1:")
print(" ".join(chunk1_words[:60]))

print("Min chunk size:", min(sizes))
print("Max chunk size:", max(sizes))
print("Avg chunk size:", sum(sizes) / len(sizes))

# 2. عينة من chunks
print("\n===== SAMPLE 1 =====")
print(data[0]["chunk_text"][:500])

print("\n===== SAMPLE 2 =====")
print(data[1]["chunk_text"][:500])

# 3. فحص overlap (اختياري بس مهم)
print("\nChecking overlap sample:")
print(data[0]["chunk_text"][-50:])
print(data[1]["chunk_text"][:50])

