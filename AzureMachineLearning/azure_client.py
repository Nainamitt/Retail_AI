import requests
from AzureMachineLearning.config import AZURE_ENDPOINT, AZURE_API_KEY
from AzureMachineLearning.schemas import UserInput


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AZURE_API_KEY}"
}

def build_azure_payload(data: UserInput):

    
    return {
        "Inputs": {
            "input1": [
                {
                    
                    "Price": float(data.Price),
                    "Stock": int(data.Stock),
                    "Rating": float(data.Rating),
                    "Reviews_Count": int(data.Reviews_Count),
                    "Previous_Sales": float(data.Previous_Sales),
                    "Discount_Percentage": float(data.Discount_Percentage),
                    "Transaction_Quantity": int(data.Transaction_Quantity),
                    "Holiday_Flag": int(data.Holiday_Flag),
                    "Month": int(data.Month),
                    
                     "Category": str(data.Category),
                    "Brand": str(data.Brand),
                    "Region": str(data.Region),

                    

                    "Store_ID": 1,               
                    "Product_ID": 0,            
                    "Customer_ID": "C001",      
                    "Transaction_ID": "T001",
                    "Product_Name": "NA",
                    "Date": "2026-05-26",
                    "Temperature": 28.0,
                    "Fuel_Price": 100.0,
                    "CPI": 210.0,
                    "Unemployment": 5.0,
                    "Day": 26,
                    "Day_Name": "Tuesday",
                    "Sales_Category": "NA",
                    "Revenue_PerUnit": float(data.Price),
                    "Inventory_Status": "Available",

                    
                    "Sales_Growth_Percentage": 0,
                    "Total_Amount": data.Price * data.Transaction_Quantity,
                    "Current_Sales": 0,
                    "Demand_Level": "Medium",
                    "Fraud_Flag": 0,
                    "Year": 2026,
                    "Inventory_Risk": "Low",
                    "AI_Recommendation": 0,
                    "Payment_Method": "UPI",
                    "Customer_Query": "API request"
                }
            ]
        }
    }




def call_azure(payload):

    response = requests.post(
        AZURE_ENDPOINT,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code == 200:
        return response.json()

    return {
        "error": "Azure API failed",
        "status_code": response.status_code,
        "response": response.text
    }