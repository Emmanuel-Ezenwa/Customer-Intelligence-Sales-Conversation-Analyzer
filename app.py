import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
 
# load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

def predict_intent(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

def buyer_score(intent):
    scores = {
        "buying": 90,
        "negotiation": 70,
        "inquiry": 40,
        "not_serious": 10
    }
    return scores.get(intent, 0)

# UI
st.title("Emmanuel AI Sales Analyzer")
st.write("Analyze customer messages and predict buying intent")
st.set_page_config(page_title="Ezenwa AI", page_icon="🔥")
st.subheader("AI-powered customer intent analyzer for smarter sales decisions")

user_input = st.text_area("Enter customer message:")

if st.button("Analyze"):
    intent = predict_intent(user_input)
    score = buyer_score(intent)

    st.subheader("Result")
    st.write("Intent:", intent)
    st.write("Buyer Score:", score)
