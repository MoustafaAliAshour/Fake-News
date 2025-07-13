import streamlit as st
import joblib
import re
import string

# -------- English UI Text --------
txt = {
    "title": "📰 Fake News Detection App",
    "subtitle": "Detect whether a news article is **Real or Fake** using multiple ML models.",
    "enter_text": "📝 Enter News Article Content",
    "choose_model": "🤖 Choose a Model",
    "predict": "🔍 Predict",
    "empty_warning": "⚠️ Please enter some text to classify.",
    "result_prefix": "Prediction using"
}

# -------- Preprocessing Function --------
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text.strip()

# -------- Load Models & Vectorizer --------
vectorizer = joblib.load("models/vectorizer.pkl")
models = {
    "Logistic Regression": joblib.load("models/LR_model.joblib"),
    "Decision Tree": joblib.load("models/DT_model.joblib"),
    "Random Forest": joblib.load("models/RFC_model.joblib"),
    "Gradient Boosting": joblib.load("models/GBC_model.joblib")
}

# -------- UI --------
st.title(txt["title"])
st.markdown(txt["subtitle"])

input_text = st.text_area(txt["enter_text"])
selected_model = st.selectbox(txt["choose_model"], list(models.keys()))

# -------- Predict Button --------
if st.button(txt["predict"]):
    if not input_text.strip():
        st.warning(txt["empty_warning"])
    else:
        model = models[selected_model]
        cleaned = wordopt(input_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        label = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        st.success(f"{txt['result_prefix']} {selected_model}: {label}")
# -------- Footer --------
st.markdown("""
    <style>
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 1rem;
            background-color: #f1f1f1;
        }
    </style>
    <footer>
        <p>Made with ❤️ by [Moustafa Ali Ashour]</p>
    </footer>""")