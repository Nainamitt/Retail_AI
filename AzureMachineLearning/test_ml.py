from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


valid_input = {
    "Price": 120000,
    "Stock": 5,
    "Rating": 4.9,
    "Reviews_Count": 5000,
    "Previous_Sales": 90000,
    "Discount_Percentage": 5,
    "Transaction_Quantity": 1,
    "Holiday_Flag": 0,
    "Month": 12,
    "Category": "Mobiles",
    "Brand": "Apple",
    "Region": "West"
}



def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Retail Sales Prediction API Running"



def test_predict_status():

    response = client.post("/predict1", json=valid_input)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200



def test_response_key():

    response = client.post("/predict1", json=valid_input)

    json_data = response.json()

    assert "Predicted_Current_Sales" in json_data



def test_scored_label():

    response = client.post("/predict1", json=valid_input)

    json_data = response.json()

    scored_label = json_data["Predicted_Current_Sales"]["Results"]["WebServiceOutput0"][0]["Scored Labels"]

    assert scored_label is not None
    assert isinstance(scored_label, (float, int))



def test_invalid_input():

    response = client.post("/predict1", json={})

    assert response.status_code == 422