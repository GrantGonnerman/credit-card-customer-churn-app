# Credit Card Churn Predictor

**🔗 Live Demo:** [https://credit-card-customer-churn-app-grantg.streamlit.app/](https://credit-card-customer-churn-app-grantg.streamlit.app/)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-5C5C5C?style=for-the-badge&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-FF6F00?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 📋 Project Overview

**Interactive web application** that predicts credit card customer churn using a powerful **Voting Classifier ensemble**.

This deployed app was built from my full end-to-end machine learning project. It allows users to input customer details and receive **instant churn risk predictions** with clear business recommendations.

The **[full project repository](https://github.com/GrantGonnerman/credit-card-customer-attrition)** contains in-depth EDA, extensive model experimentation, feature engineering details, and full reports.

---

## ✨ Key Highlights

- **Model**: Soft Voting Classifier (Gradient Boosting + HistGradientBoosting + LightGBM + XGBoost + CatBoost)
- **Feature Selection**: RFECV (5-fold, F1-score) – kept features selected ≥90% of the time
- **Feature Engineering**: 4 custom interaction terms
- **Performance**: 98% Accuracy | 93% Recall on Churn class
- **Deployment**: Live Streamlit web app

---

## 🎯 Business Value

This tool helps credit card issuers:
- Identify at-risk customers **early**
- Prioritize retention campaigns effectively
- Reduce expensive customer acquisition costs
- Support data-driven retention strategies

---

## 📸 Screenshots

**Main Interface**  
![Main Interface](screenshots/main-interface.png)

**High Churn Risk Prediction**  
![High Risk](screenshots/high-risk.png)

**Low Churn Risk Prediction**  
![Low Risk](screenshots/low-risk.png)

---

## 🗂️ Dataset

- **Source**: [Kaggle - Credit Card Customers](https://www.kaggle.com/datasets/thedevastator/predicting-credit-card-customer-attrition-with-m)
- **Target**: `Attrition_Flag` (Existing Customer vs Attrited Customer)

---

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python, scikit-learn, XGBoost, LightGBM, CatBoost
- **Deployment**: Streamlit Community Cloud
- **Tools**: pandas, joblib, RFECV

---

## 📁 Project Structure

```bash
credit-card-customer-churn-app/
├── app.py                  # Main Streamlit app
├── model.pkl               # Trained Voting Classifier
├── requirements.txt
├── README.md
├── notebooks/              # Full modeling notebooks
├── data/                   # Sample data (optional)
└── screenshots/

---

## 🚀 How to Run Locally

git clone https://github.com/GrantGonnerman/credit-card-customer-churn-app.git
cd credit-card-customer-churn-app

pip install -r requirements.txt
streamlit run app.py
