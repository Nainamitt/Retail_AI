from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("key"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("endpoint")
)




def data_analyst_agent(query, data):

    prompt = f"""
You are a strict Retail Data Analyst.

RULES:
- Use ONLY the provided data.
- Do NOT assume external information.
- If answer is not in data, say: "INSUFFICIENT DATA".
- Be precise and data-driven.

-------------------------
DATA (ONLY SOURCE OF TRUTH):
{data}
-------------------------

USER QUESTION:
{query}

-------------------------
INSTRUCTIONS:
1. Analyze the data carefully.
2. Extract only relevant insights.
3. Provide final answer clearly.
4. If possible, include numbers or evidence from data.
5. Do not hallucinate.

FORMAT:
Answer:
Reason:
Confidence (High/Medium/Low):
"""

    response = client.chat.completions.create(
        model=os.getenv("deploymentName"),
        messages=[
            {"role": "system", "content": "You are a strict and accurate retail data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0  # IMPORTANT for correctness
    )

    return response.choices[0].message.content
