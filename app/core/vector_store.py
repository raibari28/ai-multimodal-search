# vector_store.py
import faiss
import numpy as np

dimension = 512
index = faiss.IndexFlatL2(dimension)

documents = []

def add_vector(vector, metadata):
    index.add(np.array([vector]))
    documents.append(metadata)

def search_vector(query_vector, k=5):
    D, I = index.search(np.array([query_vector]), k)
    return [documents[i] for i in I[0]]
