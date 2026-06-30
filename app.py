import streamlit as st
import pandas as pd
import joblib
import sys
import importlib.util

print("Python:", sys.version)
print("joblib spec:", importlib.util.find_spec("joblib"))
st.set_page_config(
    page_title="Credit Card Churn Predictor",
    layout="wide",
    page_icon="🔮"
)

st.title("🔮 Credit Card Customer Churn Predictor")
st.markdown("**Voting Classifier** (Gradient Boosting + HistGB + LightGBM + XGBoost + CatBoost) — Data Science Portfolio Project")

# Load model
@st.cache_resource
def load_model():
    try:
        return joblib.load("models/model.pkl")
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()

model = load_model()

st.sidebar.header("Customer Information")

# === Input Fields ===
age = st.sidebar.slider("Customer Age", 26, 73, 45)
months_on_book = st.sidebar.slider("Months on Book", 13, 56, 36)

relationship_count = st.sidebar.slider("Total Relationship Count (Products)", 1, 6, 3)
revolving_bal = st.sidebar.slider("Total Revolving Balance ($)", 0, 2517, 1000)
amt_change = st.sidebar.slider("Total Amt Chng Q4/Q1", 0.0, 3.397, 0.8, step=0.01)

trans_amt = st.sidebar.slider("Total Transaction Amount ($)", 510, 18484, 10000)
trans_ct = st.sidebar.slider("Total Transaction Count", 10, 139, 60)
ct_change = st.sidebar.slider("Total Ct Chng Q4/Q1", 0.0, 3.714, 1.0, step=0.01)

inactive_months = st.sidebar.slider("Months Inactive (Last 12 mon)", 0, 6, 2)
contacts = st.sidebar.slider("Contacts Count (Last 12 mon)", 0, 6, 2)
util_ratio = st.sidebar.slider("Avg Utilization Ratio", 0.0, 1.0, 0.4, step=0.01)
open_to_buy = st.sidebar.slider("Avg Open To Buy ($)", 3, 34516, 15000)

# Auto-calculate interactions using exact formulas
inter1 = age * months_on_book
inter2 = revolving_bal * util_ratio
inter3 = trans_amt * trans_ct
inter4 = util_ratio * open_to_buy

st.sidebar.markdown(f"**Auto-calculated Interactions:**")
st.sidebar.write(f"interaction_1: **{inter1:,.0f}**")
st.sidebar.write(f"interaction_2: **{inter2:,.2f}**")
st.sidebar.write(f"interaction_3: **{inter3:,.0f}**")
st.sidebar.write(f"interaction_4: **{inter4:,.2f}**")

if st.sidebar.button("🔍 Predict Churn", type="primary", use_container_width=True):
    input_df = pd.DataFrame([{
        'Customer_Age': age,
        'Total_Relationship_Count': relationship_count,
        'Total_Revolving_Bal': revolving_bal,
        'Total_Amt_Chng_Q4_Q1': amt_change,
        'Total_Trans_Amt': trans_amt,
        'interaction_1': inter1,
        'interaction_2': inter2,
        'Total_Trans_Ct': trans_ct,
        'Total_Ct_Chng_Q4_Q1': ct_change,
        'interaction_3': inter3,
        'interaction_4': inter4,
        'Months_Inactive_12_mon': inactive_months,
        'Contacts_Count_12_mon': contacts,
        'Avg_Utilization_Ratio': util_ratio
    }])

    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]

    # Display Prediction
    col1, col2 = st.columns([3, 1])
    with col1:
        if pred == 1:
            st.error(f"**HIGH CHURN RISK** ({proba:.1%} probability)")
            st.markdown("**Action**: Immediate retention campaign recommended.")
        else:
            st.success(f"**LOW CHURN RISK** ({proba:.1%} probability)")
            st.markdown("Customer appears stable.")
    
    with col2:
        st.metric("Churn Probability", f"{proba:.1%}")
        st.metric("Prediction", "Churn" if pred == 1 else "Retain")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Model Performance", "ℹ️ About", "💡 Insights"])

with tab1:
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Accuracy", "97%")
    col_m2.metric("Recall (Churn)", "90%")
    col_m3.metric("ROC AUC", "99%") 

with tab2:
    st.markdown("""
    - **Dataset**: Kaggle Credit Card Customers  
    - **Model**: Soft Voting Classifier (5 Boosting Models)  
    - **Feature Selection**: RFECV (5 folds, F1-score) — kept features selected ≥90% of the time  
    - **Key Engineering**: 4 Custom Interaction Features
    """)

with tab3:
    st.info("**High Risk Signals**")
    st.markdown("""
    - High inactivity + low transaction activity  
    - Declining transaction amount/count  
    - Low relationship count + frequent bank contacts
    """)
