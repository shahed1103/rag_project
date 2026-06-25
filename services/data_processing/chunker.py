def chunk_text(text, chunk_size=250, overlap=40):
    words = text.split()

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])

        # 🔥 IMPORTANT FIX
        if len(chunk.split()) < 30:
            start += chunk_size - overlap
            continue

        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks