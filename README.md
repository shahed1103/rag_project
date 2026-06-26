# Arabic Information Retrieval System using RAG

## Overview

This project implements an **Arabic Information Retrieval (IR) System** integrated with a **Retrieval-Augmented Generation (RAG)** pipeline.

The system retrieves the most relevant Arabic text chunks from a custom-built dataset using three retrieval techniques:

- TF-IDF
- BM25
- Dense Vector Search (Sentence Transformers + Qdrant)

The retrieved results are then fused using **Reciprocal Rank Fusion (RRF)** before being passed to **Google Gemini** to generate an answer grounded only in the retrieved knowledge.

The project follows a **Service-Oriented Architecture (SOA)** where each component is implemented as an independent service.

---

# Features

- Arabic text preprocessing
- Custom dataset construction
- Automatic chunk generation
- TF-IDF indexing
- BM25 indexing
- Dense Embedding indexing
- Qdrant vector database
- Hybrid Retrieval
- Reciprocal Rank Fusion (RRF)
- Prompt Engineering
- Google Gemini Integration
- FastAPI REST API
- Evaluation using IR metrics

---

# Dataset

The dataset was manually constructed from Arabic Islamic books.

Dataset statistics:

- 77 Chapters
- 1852 Text Chunks

Each chunk contains metadata including:

- Book ID
- Chapter ID
- Chapter Title
- Chunk ID
- Chunk Text

---

# Project Structure

```text
project/

│

├── data/

│ ├── Books/

│ │ ├── Book1/

│ │ ├── Book2/

│ │ └── ...

│ └── metadata/

│ └── chapters_metadata.json

│

├── output/

│ ├── tfidf/

│ │ ├── tfidf_matrix.pkl

│ │ ├── tfidf_metadata.json

│ │ └── tfidf_vectorizer.pkl
 
│ ├── bm25/

│ │ ├── bm25_metadata.json

│ │ └── bm25_model.pkl

│ ├── embeddings/

│ │ ├── embeddings.npy

│ │ └── embeddings_metadata.json

│ ├── qdrant/

│ │ └── meta.json

│ ├── chunked_dataset.json

│ ├── dataset.json

│ ├── evaluation_results.csv

│

├── services/

│

├── data_processing/

│ ├── text_cleaner.py

│ ├── chunker.py

│ ├── run_chunking.py

│ ├── docx_utils.py

│ └── build_dataset.py

│

├── indexing/

│ ├── build_tfidf.py

│ ├── build_bm25.py

│ ├── build_embeddings.py

│ └── build_qdrant.py

│

├── retrieval/

│ ├── tfidf_search.py

│ ├── bm25_search.py

│ ├── vector_search.py

│ ├── query_bm25.py

│ ├── query_embedding.py

│ ├── query_tfidf.py

│ ├── fusion_search.py

│ └── query_processor.py

│

├── rag/

│ ├── prompt_builder.py

│ ├── context_builder.py

│ └── rag_pipeline.py

│

├── llm/

│ └── gemini_client.py

│

├── evaluation/

│ ├── ground_truth.json

│ ├── evaluate.py

│ └── evaluation_runner.py

│

├── api_gateway/

│ └── api.py

│

└── requirements.txt
```

---

# System Architecture

```
User

│

▼

FastAPI

│

▼

RAG Pipeline

│

├──────────────┐

▼ ▼ ▼

TF-IDF BM25 Vector Search

│ │ │

└──────┬───────┘

▼

Fusion (RRF)

▼

Prompt Builder

▼

Google Gemini

▼

Final Answer
```

---

# Technologies

- Python
- FastAPI
- Sentence Transformers
- Qdrant
- Scikit-learn
- Rank-BM25
- NumPy
- Google Gemini API

---

# Installation

Clone the repository

```bash
git clone https://github.com/your_username/your_repository.git
```

Create environment

```bash
python -m venv ir_env
```

Activate environment

Windows

```bash
ir_env\Scripts\activate
```

Linux

```bash
source ir_env/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Build Indexes

TF-IDF

```bash
python -m services.indexing.build_tfidf
```

BM25

```bash
python -m services.indexing.build_bm25
```

Embeddings

```bash
python -m services.indexing.build_embeddings
```

Qdrant

```bash
python -m services.indexing.build_qdrant
```

---

# Run API

```bash
uvicorn services.api_gateway.api:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# API

POST

```
/ask
```

Example Request

```json
{
    "question":"ما هو تعريف الفقه؟"
}
```

Example Response

```json
{
    "answer":"...",
    "sources":[
        {
            "book":"Book1",
            "chapter":"تعريف الفقه"
        }
    ]
}
```

---

# Evaluation

The retrieval system is evaluated using:

- Precision@10
- Recall@10
- MAP
- nDCG

Evaluation can be executed using

```bash
python -m services.evaluation.evaluation_runner
```

---

# Retrieval Pipeline

```
Question

↓

Query Processing

↓

TF-IDF Search

↓

BM25 Search

↓

Vector Search

↓

Fusion (RRF)

↓

Top Chunks

↓

Prompt Builder

↓

Google Gemini

↓

Answer
```

---

# Future Improvements

- Cross Encoder Re-ranking
- Query Expansion
- Better Arabic Embedding Models
- User Feedback Loop
- Multi-document Summarization

---

# Author

Shahed Alsoliman

Arabic Information Retrieval System with Retrieval-Augmented Generation (RAG)
