from flask import Flask, request, jsonify, make_response
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        # Preflight request handling
        response = make_response()
    else:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            response = make_response(jsonify({"error": "No text provided"}), 400)
        else:
            X = vectorizer.transform([text])
            prediction = model.predict(X)[0]
            result = "spam" if prediction == 1 else "ham"
            response = make_response(jsonify({"result": result}), 200)

    # ✅ Inject CORS headers
    response.headers["Access-Control-Allow-Origin"] = "chrome-extension://ccknlkpmdfadjjhfdogbfipapagemmbp"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# For local dev
if __name__ == "__main__":
    app.run(debug=True)
