from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


from dotenv import load_dotenv
import os

load_dotenv()

key1 = os.getenv("key1")
endpoint1 = os.getenv("endpoint1")

client = DocumentAnalysisClient(
    endpoint=endpoint1,
    credential=AzureKeyCredential(key1)
)

def extract_pdf(file_path):

    with open(file_path, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-document",
            document=f
        )

        result = poller.result()

    text = ""

    for page in result.pages:
        for line in page.lines:
            text += line.content + "\n"

    return text


# print(extract_pdf("D:\SprintProject\cognitiveServices/report.jpeg"))
print(extract_pdf("D:\SprintProject\cognitiveServices/projectcase.pdf"))