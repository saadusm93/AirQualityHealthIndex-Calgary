# AirQualityHealthIndex-Calgary
A streamlit app that uses SARIMAX to predict air quality in Calgary for the next 'n' days. 

# Calgary AQHI Forecasting Tool

This project is a machine learning-based forecasting tool for predicting Calgary’s Air Quality Health Index (AQHI) using time series modeling. The goal is to help individuals—especially those with respiratory conditions—make informed decisions about outdoor activity based on short-term air quality forecasts.

## Project Overview

The tool uses a SARIMAX model (Seasonal AutoRegressive Integrated Moving Average with eXogenous variables) to predict AQHI levels for up to 72 hours in advance. The model integrates both temporal features and exogenous environmental data such as weather conditions and pollutant concentrations.

This project was originally deployed as a Streamlit app and is now being adapted into a WhatsApp-based AI chatbot for broader accessibility and intuitive use.

### Key Objectives
- Forecast AQHI with a multivariate time series model
- Visualize air quality trends and provide health advisories
- Make the tool accessible through both web and messaging platforms

## Features Used in the Model

The forecasting model uses the following features:

- Carbon Monoxide  
- Nitrogen Dioxide  
- Outdoor Temperature  
- Ozone  
- PM10 Mass  
- PM2.5 Mass  
- Relative Humidity  
- Wind Speed  
- Month Num (Numeric month indicator for seasonality)  
- Is Weekend (Binary flag for weekends)

## Technologies Used

- Python, pandas, NumPy  
- SARIMAX (from statsmodels)  
- Streamlit for building the web app  
- Matplotlib / Plotly for interactive visualizations  
- scikit-learn for preprocessing and evaluation  
- (Planned) OpenAI API + WhatsApp Business API for chatbot deployment

## Forecasting Output

The model predicts AQHI levels for the next 24–72 hours and classifies health risk levels as:

- Low (1–3): Ideal for outdoor activities  
- Moderate (4–6): Caution for sensitive groups  
- High (7–10): Limit outdoor exertion  
- Very High (10+): Avoid outdoor activity

## Getting Started

To run this project locally:

1. Clone the repo:
   ```bash
   git clone https://github.com/saadusm93/AirQualityHealthIndex-Calgary.git 
   cd aqhi-forecasting

2. Create a virtual environment and install dependencies:
   ```bash python -m venv venv
   source venv/bin/activate
   venv\Scripts\activate (Windows)
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py

6. To retrain or test the model:
   ```bash
   python forecast_aqhi.py


## Future Roadmap
    Integrate with WhatsApp for conversational AQHI updates
    Expand coverage to other cities with available AQHI data
    Add anomaly detection for sudden air quality changes
    Implement real-time alert system via SMS or email
