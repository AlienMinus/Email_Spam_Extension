# test_api.py
import requests

response = requests.post(
    "http://127.0.0.1:5000/predict",
    json={"text": "Win a free iPhone now!"}
)

print("✅ Prediction:", response.json())
