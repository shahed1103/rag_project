from services.retrieval.fusion_search import fusion_search
from services.rag.prompt_builder import build_prompt
from services.llm.gemini_client import ask_gemini
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

with open(
   BASE_DIR / "data" / "metadata" / "chapters_metadata.json",
    "r",
    encoding="utf-8"
) as f:
    metadata = json.load(f)

def ask(question: str):

    # retrieve
    chunks = fusion_search(
        question,
        top_k=5
    )

    # build prompt
    prompt = build_prompt(
        question,
        chunks
    )

    # llm
    answer = ask_gemini(prompt)

    # sources = []

    # for chunk in chunks:

    #     sources.append({
    #         "book_id": chunk["book_id"],
    #         "chapter_id": chunk["chapter_id"],
    #         "chapter_title": chunk["chapter_title"]
    #     })
    sources_map = {}

    for chunk in chunks:

        key = (chunk["book_id"], chunk["chapter_id"])

        chapter_meta = metadata.get(chunk["book_id"], {}).get(chunk["chapter_id"], {})


        if key not in sources_map:
            sources_map[key] = {
                "book_id": chunk["book_id"],
                "chapter_id": chunk["chapter_id"],
                "chapter_title": chunk["chapter_title"],
                "video_youtube_url": chapter_meta.get("youtube_url", ""),
            }

    sources = list(sources_map.values())

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }

