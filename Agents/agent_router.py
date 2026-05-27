from Agents.data_agent import data_analyst_agent
from Agents.document_agent import document_agent
from Agents.ml_agent import ml_agent

def route_agent(query):

    query = query.lower()

    if "sales" in query:
        return data_analyst_agent(query, "Retail data")

    elif "inventory" in query:
        return document_agent(query)

    elif "prediction" in query:
        return ml_agent("High Demand")

    else:
        return "No suitable agent found"