import requests
from dotenv import load_dotenv
import os

load_dotenv()

key1 = os.getenv("key1")
endpoint1 = os.getenv("endpoint1")

vision_url = endpoint1 + "vision/v3.2/analyze"

def analyze_image(image_path):

    headers = {
        "Ocp-Apim-Subscription-Key": key1,
        "Content-Type": "application/octet-stream"
    }

    params = {
        "visualFeatures": "Description,Objects,Tags"
    }

    with open(image_path, "rb") as image_data:
        response = requests.post(
            vision_url,
            headers=headers,
            params=params,
            data=image_data  
        )

    return response.json()


print(analyze_image("D:\SprintProject\cognitiveServices/image.jpeg"))