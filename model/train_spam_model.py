import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
df = pd.read_csv("../dataset/spam.csv", encoding='latin-1')
print("Raw Columns:", df.columns.tolist())
print("Total Rows (raw):", len(df))

# Normalize labels
df['label'] = df['label'].astype(str).str.strip().str.lower()

# Clean text column
df['text'] = df['text'].astype(str).str.strip()
df = df.dropna(subset=['label', 'text'])
df = df[df['text'] != ""]
df = df[df['label'].isin(['ham', 'spam'])]  # case-insensitive now
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df = df.reset_index(drop=True)

# Safety check
if df.empty:
    raise ValueError("❌ Dataset became empty after filtering. Check label values.")
print("✅ Total Rows (cleaned):", len(df))
print(df.sample(3))

# Vectorization
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['text'])
y = df['label']

# Model training
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(tfidf, "vectorizer.pkl")
print("✅ Model trained and saved successfully.")
