from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert "status" in response.json()

def test_predict():
    payload = {
        "Price": 1000,
        "Discount": 10,
        "Inventory": 50,
        "Category": "Electronics",
        "Brand": "Samsung",
        "Region": "India",
        "Demand_Level": "High",
        "Inventory_Risk": "Low",
        "Payment_Method": "UPI"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()

def test_search():
    response = client.post("/search", json={"query": "laptop"})

    assert response.status_code == 200
    assert "results" in response.json()



def test_agent():
    payload = {
        "message": "What are today's sales trends?"
    }

    response = client.post("/agent", json=payload)

    assert response.status_code == 200
    assert "agent_response" in response.json()


def test_ingest():
    payload = {
        "id": 101,
        "text": "Samsung laptop demand is increasing",
        "category": "Electronics"
    }

    response = client.post("/ingest", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert data["message"] == "Data ingested successfully"
    assert "inserted_id" in data