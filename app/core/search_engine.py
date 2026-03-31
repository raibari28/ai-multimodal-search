# update search_engine.py
from app.core.embeddings import fake_embedding
from app.core.vector_store import search_vector

def multimodal_search(query: str, search_type: str = "text"):
    q_vec = fake_embedding(query)
    results = search_vector(q_vec)

    return {
        "query": query,
        "results": results
    }
