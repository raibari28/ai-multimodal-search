def multimodal_search(query: str, search_type: str = "text"):
    # Replace this later with real embeddings / models
    return {
        "query": query,
        "type": search_type,
        "results": [
            f"Sample result 1 for {query}",
            f"Sample result 2 for {query}"
        ]
    }
