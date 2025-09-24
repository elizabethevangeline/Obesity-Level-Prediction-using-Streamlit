from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pickle
import pandas as pd

# Load model pipeline
with open("best_model_xgboost.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Obesity Prediction API")


class GenderEnum(str, Enum):
    Female = "Female"
    Male = "Male"

class YesNoEnum(str, Enum):
    yes = "yes"
    no = "no"

class CAECEnum(str, Enum):
    no = "no"
    Sometimes = "Sometimes"
    Frequently = "Frequently"
    Always = "Always"

class CALCEnum(str, Enum):
    no = "no"
    Sometimes = "Sometimes"
    Frequently = "Frequently"
    Always = "Always"

class MTRANS_Enum(str, Enum):
    Automobile = "Automobile"
    Bike = "Bike"
    Motorbike = "Motorbike"
    Public_Transportation = "Public_Transportation"
    Walking = "Walking"


class ObesityInput(BaseModel):
    Gender: GenderEnum
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: YesNoEnum
    FAVC: YesNoEnum
    FCVC: float
    NCP: float
    CAEC: CAECEnum
    SMOKE: YesNoEnum
    CH2O: float
    SCC: YesNoEnum
    FAF: float
    TUE: float
    CALC: CALCEnum
    MTRANS: MTRANS_Enum

# --- Endpoint dasar ---
@app.get("/")
def root():
    return {"message": "Obesity Prediction API with Enum is running."}

# --- Endpoint prediksi utama ---
@app.post("/predict")
def predict(data: ObesityInput):
    # Ambil input user
    input_dict = data.dict()

    # Mapping manual: Gender (karena waktu training kamu encode sendiri)
    input_dict["Gender"] = 0 if input_dict["Gender"] == "Female" else 1

    # Pastikan urutan kolom sesuai model training
    ordered_columns = [
        "Gender",
        "Age",
        "Height",
        "Weight",
        "family_history_with_overweight",
        "FAVC",
        "FCVC",
        "NCP",
        "CAEC",
        "SMOKE",
        "CH2O",
        "SCC",
        "FAF",
        "TUE",
        "CALC",
        "MTRANS"
    ]

    input_df = pd.DataFrame([input_dict])[ordered_columns]

    # Prediksi
    prediction = model.predict(input_df)[0]

    # Label hasil prediksi
    label_map = {
        0: "Insufficient_Weight",
        1: "Normal_Weight",
        2: "Obesity_Type_I",
        3: "Obesity_Type_II",
        4: "Obesity_Type_III",
        5: "Overweight_Level_I",
        6: "Overweight_Level_II"
    }

    return {
        "prediction_code": int(prediction),
        "prediction_label": label_map.get(prediction, "Unknown")
    }