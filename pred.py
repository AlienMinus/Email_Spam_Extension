# pred.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- CONFIG ---
CSV_PATH = "dataset/spam.csv"
MODEL_PATH = "model/spam_model.pkl"
VEC_PATH = "model/vectorizer.pkl"
TEST_INPUT = "FreeMsg: Win a free iPhone now! Just reply YES to claim."  # Set to None to skip

# --- LOAD DATA ---
print("📦 Loading dataset...")
df_raw = pd.read_csv(CSV_PATH, encoding='latin-1')
print("🧾 Raw Columns:", df_raw.columns.tolist())
print("🔢 Raw Shape:", df_raw.shape)
print("🧪 Sample:\n", df_raw.head(3))

# Proceed only if 'label' and 'text' are present
if not all(col in df_raw.columns for col in ['label', 'text']):
    raise ValueError("❌ Columns 'label' and 'text' not found in dataset.")

df = df_raw[['label', 'text']].dropna()
df['label'] = df['label'].str.strip().str.lower()  # 🔥 Normalize labels
df = df[df['label'].isin(['spam', 'ham'])]


print("✅ Cleaned Shape:", df.shape)
if df.empty:
    raise ValueError("❌ Dataset is empty after filtering for spam/ham. Check your label values.")

print(f"✅ Loaded {len(df)} rows.")
print(df.sample(2), '\n')

# --- LOAD MODEL ---
print("📥 Loading model & vectorizer...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VEC_PATH)
print("✅ Model and vectorizer loaded.\n")

# --- ENCODE LABELS ---
le = LabelEncoder()
df['label_num'] = le.fit_transform(df['label'])  # spam=1, ham=0

# --- TRANSFORM TEXT ---
X = vectorizer.transform(df['text'])
y = df['label_num']

# --- SPLIT & EVALUATE ---
print("🧪 Evaluating model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
y_pred = model.predict(X_test)

print("✅ Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred, target_names=['ham', 'spam']))
print("🧾 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# --- PREDICT CUSTOM TEXT ---
if TEST_INPUT:
    print("\n📨 Testing input:")
    print("Text:", TEST_INPUT)
    input_vec = vectorizer.transform([TEST_INPUT])
    prediction = model.predict(input_vec)[0]
    label = le.inverse_transform([prediction])[0]
    print(f"✅ Prediction: This message is classified as **{label.upper()}**.")
