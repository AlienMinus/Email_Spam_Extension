# test_api.py
import requests

response = requests.post(
    "https://emailspamextension-6m20m568p-alienminus-projects.vercel.app/predict",
    json={"text": "Win a free iPhone now!"}
)

print("✅ Prediction:", response.json())
