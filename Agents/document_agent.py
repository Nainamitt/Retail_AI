from openai import AzureOpenAI
import os
import numpy as np
from Agents.embeddings import get_embedding
from Agents.vector_store import index, documents
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("key"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("endpoint")
)

def retrieve(query):

    query_vector = np.array(
        [get_embedding(query)]
    ).astype("float32")

    distances, indices = index.search(query_vector, k=2)

    return [documents[i] for i in indices[0]]



def document_agent(query):

    docs = retrieve(query)

    context = "\n\n".join([str(d) for d in docs])

    prompt = f"""
You are a strict Retrieval-Based QA Assistant.

RULES:
- Answer ONLY using the provided documents.
- If answer is not in documents, say: "I don't have enough information in the provided documents."
- Do NOT use outside knowledge.
- Do NOT guess.

-------------------------
DOCUMENTS:
{context}
-------------------------

QUESTION:
{query}

-------------------------
INSTRUCTIONS:
1. Read documents carefully.
2. Extract exact relevant information.
3. If multiple docs conflict, mention that.
4. Provide final clear answer.

FORMAT:
Answer:
Source Evidence:
Confidence: High/Medium/Low
"""

    response = client.chat.completions.create(
        model=os.getenv("deploymentName"),
        messages=[
            {"role": "system", "content": "You are a precise and strict document-based QA assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content