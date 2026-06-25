def build_context(chunks):

    context_parts = []

    for i, chunk in enumerate(chunks, start=1):

        context_parts.append(
            f"""
[Source {i}]
Book: {chunk["book_id"]}
Chapter: {chunk["chapter_title"]}

{chunk["text"]}
"""
        )

    return "\n".join(context_parts)
