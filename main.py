from fastapi import FastAPI , HTTPException
import pandas as pd
import joblib
import numpy as np
from schemas import DataInput,PredictionInput, SearchQuery, AgentInput , SalesData , AnalystRequest , DocRequest , MLRequest
from model import make_prediction
from data_store import DATA_STORE
from agent import run_agent
from database import prediction_collection
from Agents.agent_router import route_agent
from Agents.data_agent import data_analyst_agent
from Agents.document_agent import document_agent
from Agents.ml_agent import ml_agent
from fastapi import FastAPI
from AzureMachineLearning.schemas import UserInput
from AzureMachineLearning.azure_client import call_azure , build_azure_payload

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(title="RetailGPT API", version="1.0")


@app.get("/health")
def health_check():
    return {
        "status": "running",
        "total_records": len(DATA_STORE)
    }


@app.post("/predict")
def predict(data: SalesData):
    try:
        
        input_data = data.model_dump()

    
        logger.info(f"Incoming request: {input_data}")

        
        result = make_prediction(input_data)

        prediction_collection.insert_one({
            "input": input_data,
            "prediction": result
        })

        logger.info("Data saved to MongoDB successfully")

        return {
            "prediction": result , 
            "message": "Saved to MongoDB"
        }

    
    except Exception as e:
        import traceback
        print(traceback.format_exc())   

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    

@app.get("/mongo-data")
def get_mongo_data():
    data = list(prediction_collection.find({}, {"_id": 0}))
    
    return {
        "count": len(data),
        "data": data
    }



@app.post("/ingest")
def ingest_data(payload: DataInput):

    DATA_STORE.append(payload.model_dump())

    return {
        "message": "Data ingested successfully",
        "inserted_id": payload.id,
        "total_records": len(DATA_STORE)
    }



@app.get("/data")
def get_all_data():
    return {
        "data": DATA_STORE,
        "count": len(DATA_STORE)
    }



@app.post("/search")
def search(payload: SearchQuery):

    query = payload.query.lower()
    results = []

    for item in DATA_STORE:
        text = item.get("text", "").lower()

        if query in text:
            results.append(item)

    return {
        "query": payload.query,
        "count": len(results),
        "results": results
    }



@app.post("/agent")
def agent(payload: AgentInput):

    result = run_agent(payload.message)

    return {
        "input": payload.message,
        "agent_response": result
    }



@app.post("/data-analyst")
def run_data_analyst(req: AnalystRequest):
    return data_analyst_agent(req.query, req.data)


@app.post("/document")
def run_document(req: DocRequest):
    return document_agent(req.query)


@app.post("/ml")
def run_ml(req: MLRequest):
    return ml_agent(req.prediction_input)



@app.get("/")
def home():

    return {
        "message": "Retail Sales Prediction API Running"
    }


@app.post("/predict1")
def predict(data: UserInput):

    payload = build_azure_payload(data)
    result = call_azure(payload)

    return {
        "Predicted_Current_Sales": result
    }
