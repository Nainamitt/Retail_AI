from pydantic import BaseModel
from typing import List

class DataInput(BaseModel):
    id: int
    text: str
    category: str




class SearchQuery(BaseModel):
    query: str

class AgentInput(BaseModel):
    message: str


class SalesData(BaseModel):

    Price: float
    Discount: float
    Inventory: int
    Category: str
    Brand: str
    Region: str
    Demand_Level: str
    Inventory_Risk: str
    Payment_Method: str

class AnalystRequest(BaseModel):
    query: str
    data: str

class DocRequest(BaseModel):
    query: str

class PredictionInput(BaseModel):
    churn_probability: float
    threshold: float


class MLRequest(BaseModel):
    prediction_input: PredictionInput