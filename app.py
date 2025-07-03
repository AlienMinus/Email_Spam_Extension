from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["chrome-extension://ccknlkpmdfadjjhfdogbfipapagemmbp"])
  # allow all origins


# Load model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    result = "spam" if prediction == 1 else "ham"
    return jsonify({"result": result}), 200

if __name__ == "__main__":
    app.run(debug=True)

