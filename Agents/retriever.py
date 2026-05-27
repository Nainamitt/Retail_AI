import numpy as np
from Agents.embeddings import get_embedding
from Agents.vector_store import index, documents

def retrieve(query):

    query_vector = np.array(
        [get_embedding(query)]
    ).astype("float32")

    distances, indices = index.search(query_vector, k=2)

    return [documents[i] for i in indices[0]]