import os
import ssl
import nltk
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from data import intents

# Set up SSL and download NLTK data
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))

nltk.download('punkt')

# Initialize vectorizer and classifier (term frequency-inverse document frequency)
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Prepare training data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Save the model and vectorizer
joblib.dump((vectorizer, clf), 'chatbot_model.pkl')
print("Model trained and saved as 'chatbot_model.pkl'")
