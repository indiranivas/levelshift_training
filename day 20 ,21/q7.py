import streamlit as st
import joblib

model = joblib.load('model_latest.pkl')

st.title("House Price Predictor")

area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms]])[0]
    st.write(f"Predicted Price: {int(prediction)}")