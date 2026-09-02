import streamlit as st
import joblib

model = joblib.load("C:\\Users\\hasnain ali\\Desktop\\ai-journey\\07 NLP (Machine Learning)\\emotion_model.pkl")

st.title("🧠 EmotionAI")
st.write("Discover the emotion behind your words.")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text.strip():
        emotion_mapping = {
            0: "sadness",
            1: "anger",
            2: "love",
            3: "surprise",
            4: "fear",
            5: "joy"
        }
        prediction = model.predict([text])[0]
        emotion = emotion_mapping[prediction]
        probabilities = model.predict_proba([text])[0]

        st.success(f"Detected Emotion: {emotion}")

        st.write("Confidence:")
        st.progress(float(max(probabilities)))