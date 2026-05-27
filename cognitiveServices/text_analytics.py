from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

key1 = os.getenv("key1")
endpoint1 = os.getenv("endpoint1")

client = TextAnalyticsClient(
    endpoint=endpoint1,
    credential=AzureKeyCredential(key1)
)

def analyze_text(text):

    result = client.analyze_sentiment([text])[0]

    return {
        "sentiment": result.sentiment,
        "confidence": result.confidence_scores
    }

print(analyze_text("This product is very good"))