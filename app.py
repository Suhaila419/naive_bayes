import streamlit as st
import pickle

with open('naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("📧 Email Spam Filter")
email = st.text_area("Enter email content:")
if st.button("Check if Spam"):
    if email:
        vec = vectorizer.transform([email])
        pred = model.predict(vec)[0]
        st.success("Not Spam" if pred == 0 else "Spam")
    else:
        st.warning("Please type something.")

# Run Streamlit via ngrok
from pyngrok import ngrok

public_url = ngrok.connect(port=8501)
print(f"🔗 Your app is live at: {public_url}")
