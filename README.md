# Credit Card Churn Predictor

**🔗 Live Demo:** [https://credit-card-customer-churn-app-grantg.streamlit.app/](https://credit-card-customer-churn-app-grantg.streamlit.app/)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-FF6F00?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-5C5C5C?style=for-the-badge&logoColor=white)

---

## 📋 Project Overview

**Interactive web application** that predicts credit card customer churn using a high-performance **Voting Classifier ensemble**.

This project showcases the complete end-to-end data science workflow — from advanced feature engineering and rigorous model selection to production-ready deployment.

Users can input customer data and receive **instant churn risk predictions** with clear business recommendations.

---

## ✨ Key Highlights

- **Advanced Ensemble Model**: Soft Voting Classifier combining **Gradient Boosting**, **HistGradientBoosting**, **LightGBM**, **XGBoost**, and **CatBoost**
- **Robust Feature Selection**: RFECV (5-fold, F1-score) — retained only features selected ≥90% of the time
- **Domain-Driven Feature Engineering**: 4 custom interaction features
- **Production Deployment**: Fully deployed Streamlit web app (publicly accessible)
- **Focus on Business Impact**: High **Recall** on churn class (93%) to minimize missed at-risk customers

---

## 🎯 Business Value

Helps credit card companies:
- Identify high-risk customers **early**
- Prioritize retention efforts
- Reduce customer acquisition costs
- Make data-driven, proactive decisions

---

## 📸 Screenshots

![App Interface](screenshots/app_main.png)
*<img width="1913" height="884" alt="image" src="https://github.com/user-attachments/assets/05b0bbae-c819-4f86-9edc-fcdb25b9e650" />*

![Prediction Example](screenshots/prediction_high_risk.png)
*High churn risk prediction with recommendation*

![Low Risk Example](screenshots/prediction_low_risk.png)
*Low churn risk prediction*

*(Add your actual screenshots here after taking them)*


---

## 🗂️ Dataset

- **Source**: [Kaggle Credit Card Customers](https://www.kaggle.com/datasets/thedevastator/predicting-credit-card-customer-attrition-with-m)
- **Target**: `Attrition_Flag` (Existing Customer vs Attrited Customer)
- **~10,000 records** with demographic, relationship, and transaction behavior data

---

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Modeling**: scikit-learn, XGBoost, LightGBM, CatBoost
- **Deployment**: Streamlit Community Cloud
- **Other**: pandas, joblib, matplotlib

---

## 📁 Project Structure

```bash
credit-card-churn-prediction-app/
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained Voting Classifier (~ ensemble)
├── requirements.txt
├── README.md
├── notebooks/              # Original EDA + modeling
└── data/                   # Sample data (optional)
