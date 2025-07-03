# test_api.py
import requests

response = requests.post(
    "https://emailspamextension-git-main-alienminus-projects.vercel.app/predict",
    json={"text": "Win a free iPhone now!"}
)

print("✅ Prediction:", response.json())
