from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("key"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("endpoint")
)



def ml_agent(prediction):

    prompt = f"""
You are a Machine Learning Business Analyst.

You will receive a model prediction output.

RULES:
- Do NOT assume anything beyond given prediction.
- If prediction is unclear, say "Cannot interpret properly".
- Provide business insights ONLY based on prediction.
- Be practical and decision-oriented.

-------------------------
MODEL OUTPUT:
{prediction}
-------------------------

TASK:
1. Interpret what this prediction means.
2. Convert it into business impact.
3. Suggest actionable insights.
4. Mention risk if any.

FORMAT:
Interpretation:
Business Insight:
Actionable Recommendation:
Risk (if any):
Confidence (High/Medium/Low):
"""

    response = client.chat.completions.create(
        model=os.getenv("deploymentName"),
        messages=[
            {"role": "system", "content": "You are a strict ML business interpreter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content