from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("key"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("endpoint")
)