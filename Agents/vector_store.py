import faiss
import numpy as np
from Agents.embeddings import get_embedding

documents = [
    "Laptop sales increased in India",
    "Samsung inventory is low",
    "Electronics demand is high"
]

embeddings = [get_embedding(doc) for doc in documents]

dimension = len(embeddings[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))