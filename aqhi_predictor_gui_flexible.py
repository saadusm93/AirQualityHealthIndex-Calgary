
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta

# Load saved model and scaler
model = joblib.load("E:/Projects/Data/Air quality/Models/sarimax_model.pkl")
scaler = joblib.load("E:/Projects/Data/Air quality/Models/x_scaler.pkl")

st.title("AQHI Predictor for 1 to 30 Days")

num_days = st.number_input("Enter number of future days (1 to 30):", min_value=1, max_value=30, value=7)

future_inputs = []
start_date = datetime(2025, 2, 17)

for i in range(num_days):
    st.subheader(f"Day {i+1}")

    row = {}
    row['Carbon Monoxide'] = st.number_input(f"Carbon Monoxide (Day {i+1})", value=0.3)
    row['Nitrogen Dioxide'] = st.number_input(f"Nitrogen Dioxide (Day {i+1})", value=0.02)
    row['Outdoor Temperature'] = st.number_input(f"Outdoor Temperature (Day {i+1})", value=-5.0 + i)
    row['Ozone'] = st.number_input(f"Ozone (Day {i+1})", value=0.03)
    row['PM10 Mass'] = st.number_input(f"PM10 Mass (Day {i+1})", value=10.0)
    row['PM2.5 Mass'] = st.number_input(f"PM2.5 Mass (Day {i+1})", value=5.0)
    row['Relative Humidity'] = st.number_input(f"Relative Humidity (Day {i+1})", value=60.0)
    row['Wind Speed'] = st.number_input(f"Wind Speed (Day {i+1})", value=5.0)
    row['Month Num'] = st.number_input(f"Month Num (Day {i+1})", min_value=1, max_value=12, value=2)
    row['Is Weekend'] = st.selectbox(f"Is Weekend? (Day {i+1})", options=[0, 1])
    
    future_inputs.append(row)

if st.button("Predict AQHI"):
    future_df = pd.DataFrame(future_inputs)
    scaled = pd.DataFrame(scaler.transform(future_df), columns=future_df.columns)
    scaled = scaled.rolling(window=3, min_periods=1).mean()

    forecast = model.get_forecast(steps=len(scaled), exog=scaled)
    predictions = forecast.predicted_mean ** 3  # cube root inverse
    conf_int = forecast.conf_int().apply(lambda x: x ** 3)

    st.subheader("Predicted AQHI for the Next Days")
    result_df = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(len(predictions))],
        "Predicted AQHI": predictions.round(2)
    })

    def classify_risk(aqhi):
        if aqhi <= 4:
            return "Low risk"
        elif 4 < aqhi <= 6:
            return "Moderate risk"
        else:
            return "High risk"

    result_df["Risk Level"] = result_df["Predicted AQHI"].apply(classify_risk)
    st.dataframe(result_df)
