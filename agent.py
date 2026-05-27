def run_agent(message: str):

    msg = message.lower()

   
    if "add data" in msg or "ingest" in msg:
        return {
            "intent": "ingestion",
            "action": "Call /ingest API",
            "response": "Sure, I can help you add data. Send data to /ingest endpoint."
        }

    
    elif "search" in msg or "find" in msg:
        return {
            "intent": "search",
            "action": "Call /search API",
            "response": "Use /search API to find relevant documents."
        }

   
    elif "predict" in msg or "price" in msg:
        return {
            "intent": "prediction",
            "action": "Call /predict API",
            "response": "Use /predict API with features."
        }

    
    else:
        return {
            "intent": "unknown",
            "action": "none",
            "response": "I can help with ingest, search, or prediction."
        }