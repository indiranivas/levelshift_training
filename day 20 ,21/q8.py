import streamlit as st
import joblib

model = joblib.load('model_latest.pkl')

st.title("House Price Predictor")

area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)

location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])

location_mapping = {"Urban": 1, "Suburban": 2, "Rural": 3}
location_encoded = location_mapping[location]

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms, location_encoded]])[0]
    st.write(f"Predicted Price: {int(prediction)}")
    st.write(f"Encoded value = {location_encoded}")