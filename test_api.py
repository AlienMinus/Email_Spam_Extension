# test_api.py
import requests

response = requests.post(
    "http://localhost:5000/predict",
    json={"text": "Win a free iPhone now!"}
)

print("✅ Prediction:", response.json())
