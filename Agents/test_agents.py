from Agents.data_agent import data_analyst_agent
from Agents.document_agent import document_agent
from Agents.ml_agent import ml_agent


def test_data_analyst():
    print("\n===== DATA ANALYST TEST =====")

    query = "What are the top selling products?"
    data = """
    Product A: 500 sales
    Product B: 1200 sales
    Product C: 800 sales
    """

    result = data_analyst_agent(query, data)
    print(result)


def test_document_agent():
    print("\n===== DOCUMENT AGENT TEST =====")

    query = "What is return policy?"

    result = document_agent(query)
    print(result)


def test_ml_agent():
    print("\n===== ML AGENT TEST =====")

    prediction = {
        "churn_probability": 0.78,
        "threshold": 0.5
    }

    result = ml_agent(prediction)
    print(result)