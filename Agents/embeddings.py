from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("key"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("endpoint")
)


def get_embedding(text):

    response = client.embeddings.create(
        input=text,
        model= os.getenv("model")
    )

    return response.data[0].embedding