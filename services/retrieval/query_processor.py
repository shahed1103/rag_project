from services.data_processing.text_cleaner import clean_text


def process_query(query: str):
    """
    Apply the same preprocessing used on documents.
    """

    query = clean_text(query)

    tokens = query.split()

    return {
        "clean_query": query,
        "tokens": tokens
    }