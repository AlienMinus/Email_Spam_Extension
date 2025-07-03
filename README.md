# 📧 Email Spam Detection Chrome Extension

A Chrome extension powered by a Machine Learning model to detect spam emails in real-time.

## 🧠 Features
- Naive Bayes spam detection model
- TF-IDF vectorizer for email content
- Chrome extension with popup interface
- Flask backend API (localhost or cloud-deployed)

## 🛠 Folder Structure
- `/extension` → Chrome extension files
- `/model` → ML training scripts and models
- `app.py` → Flask API for predictions

## 🚀 Run Locally

1. Train the model:
```bash
cd model
python train_spam_model.py
```
2. Start Flask API:
```bash
python app.py
```
3. Load /extension in Chrome at chrome://extensions using "Load Unpacked"
4. Test with sample email texts!

## 📦 Dependencies
See requirements.txt
