import streamlit as st
import requests

# URL dari backend FastAPI kamu
API_URL = "http://127.0.0.1:8000/predict"  # Ganti sesuai alamat FastAPI kamu

st.title("Obesity Prediction App")

# Form input dari user
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", min_value=0.0)
height = st.number_input("Height (m)", min_value=0.0)
weight = st.number_input("Weight (kg)", min_value=0.0)
family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
favc = st.selectbox("Frequent High Calorie Food Consumption", ["yes", "no"])
fcvc = st.slider("Frequency of Vegetable Consumption (1-3)", 1.0, 3.0)
ncp = st.slider("Number of Meals per Day", 1.0, 4.0)
caec = st.selectbox("Consumption Between Meals", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you Smoke?", ["yes", "no"])
ch2o = st.slider("Daily Water Intake (1-3)", 1.0, 3.0)
scc = st.selectbox("Do you monitor calorie consumption?", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (0-3)", 0.0, 3.0)
tue = st.slider("Technology Usage Time (0-3)", 0.0, 3.0)
calc = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportation Mode", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])

# Kirim data ke backend
if st.button("Predict"):
    input_data = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }

    # Request ke API
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Category: {result['prediction_label']}")
    else:
        st.error("Prediction failed. Please check the API or input format.")