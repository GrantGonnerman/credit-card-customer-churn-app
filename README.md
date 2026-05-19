# Credit Card Churn Predictor

**Live Demo:** [https://credit-card-customer-churn-app-grantg.streamlit.app/](https://credit-card-customer-churn-app-grantg.streamlit.app/)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-FF6F00?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 📋 Project Overview

An interactive web application that predicts **credit card customer churn** using a powerful **Voting Classifier** ensemble. 

This tool allows users (e.g., analysts, managers, or recruiters) to input customer information and instantly receive a churn risk prediction with clear explanations.

Built as a **portfolio project** to demonstrate end-to-end data science skills — from feature engineering to model deployment.

## ✨ Features

- **Real-time Churn Prediction** using a robust ensemble model
- **Auto-calculated interaction features** based on domain logic
- Clean, intuitive interface built with **Streamlit**
- Responsive design optimized for desktop and tablets
- Professional result visualization with risk level and recommendations

## 🧠 Model Details

- **Model Type**: Soft Voting Classifier
- **Base Models**: Gradient Boosting, HistGradientBoosting, LightGBM, XGBoost, CatBoost
- **Feature Selection**: RFECV (5-fold, F1-score) — kept only features selected ≥90% of the time across runs
- **Key Engineered Features**:
  - `interaction_1` = Customer_Age × Months_on_book
  - `interaction_2` = Total_Revolving_Bal × Avg_Utilization_Ratio
  - `interaction_3` = Total_Trans_Amt × Total_Trans_Ct
  - `interaction_4` = Avg_Utilization_Ratio × Avg_Open_To_Buy

**Performance Highlights**:
- Accuracy: **98%**
- Recall (Churn class): **93%**
- Strong focus on catching at-risk customers

## 🗂️ Dataset

- **Source**: [Kaggle - Credit Card Customers](https://www.kaggle.com/datasets/thedevastator/predicting-credit-card-customer-attrition-with-m)
- **Target Variable**: `Attrition_Flag` (Existing Customer vs Attrited Customer)

## 📁 Project Structure

```bash
credit-card-churn-prediction-app/
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained Voting Classifier
├── requirements.txt
├── README.md
├── data/
│   └── sample_data.csv     # (Optional) Sample customers
└── notebooks/              # Original training & analysis
