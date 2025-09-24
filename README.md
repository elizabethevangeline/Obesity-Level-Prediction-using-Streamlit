# 🧍 Obesity Level Prediction  

## 📌 Project Overview  
This project aims to **predict obesity levels** based on individual lifestyle and physical characteristics such as age, gender, height, weight, eating habits, water intake, physical activity, and daily routines.  

The system is built end-to-end with:  
- **Data preprocessing & model training** (Jupyter Notebook)  
- **Backend REST API** (FastAPI)  
- **Frontend app** (Streamlit)  

---

## 📂 Files Description  

### 1. `MD_UAS_NO_1.ipynb`  
Notebook for data science workflow:  
- Data cleaning and preprocessing  
- Encoding categorical features (e.g., gender, family history, transportation mode)  
- Training multiple models, selecting **XGBoost** as the best performer  
- Exporting trained model as `best_model_xgboost.pkl`  

---

### 2. `main.py` (Backend API – FastAPI)  
- Loads the trained model (`best_model_xgboost.pkl`)  
- Defines an input schema using **Pydantic** and **Enum** for categorical values  
- Provides endpoints:  
  - `GET /` → health check  
  - `POST /predict` → returns obesity level prediction

---

### 3. `app.py` (Frontend – Streamlit)
- Provides a simple web UI where users can input lifestyle & body details.
- Sends data to the FastAPI backend (/predict).
- Displays predicted obesity category.

---

## ✅ Conclusion
- The project demonstrates a full ML pipeline: preprocessing → model training → deployment.
- The chosen model (XGBoost) predicts obesity categories with good accuracy.
- Users can interact with the model through a friendly Streamlit UI, making the system usable for non-technical users.
