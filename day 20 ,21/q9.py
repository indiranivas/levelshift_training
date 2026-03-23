import streamlit as st
import joblib

model = joblib.load('model_latest.pkl')

st.title("House Price Predictor")

area = st.text_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)

if st.button("Predict"):
    try:
        area_float = float(area)
        if area_float < 0:
            st.error("Invalid input")
        else:
            prediction = model.predict([[area_float, bedrooms]])[0]
            st.write(f"Predicted Price: {int(prediction)}")
    except ValueError:
        st.error("Invalid input")