from flask import Flask, request, jsonify, make_response
import joblib

app = Flask(__name__)

model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        res = make_response(jsonify({"error": "No text provided"}), 400)
    else:
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        result = "spam" if prediction == 1 else "ham"
        res = make_response(jsonify({"result": result}), 200)

    # ⬇️ Manually inject CORS headers
    res.headers["Access-Control-Allow-Origin"] = "chrome-extension://ccknlkpmdfadjjhfdogbfipapagemmbp"
    res.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    res.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return res
