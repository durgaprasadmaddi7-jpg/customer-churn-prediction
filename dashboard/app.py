import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.predict import predict_churn
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.markdown(
    "### Predict customer churn using Machine Learning"
)

st.info(
    "Enter the customer's details below and click **Predict Churn** "
    "to estimate their churn risk."
)

st.subheader("Customer Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior_citizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

st.subheader("Service Information")

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

st.subheader("Contract & Billing Information")

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=75.50,
    step=0.01
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=906.00,
    step=0.01
)

st.subheader("Churn Prediction")

if st.button("🔮 Predict Churn"):

    customer_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    probability, prediction = predict_churn(customer_data)

    st.metric(
        "Churn Probability",
        f"{probability:.1%}"
    )

    st.progress(probability)

    if probability < 0.30:
        st.success("🟢 Risk Level: Low")
    elif probability < 0.60:
        st.warning("🟡 Risk Level: Medium")
    else:
        st.error("🔴 Risk Level: High")

        st.subheader("🔍 Risk Indicators")

    risk_indicators = []

    if contract == "Month-to-month":
        risk_indicators.append(
            "Customer is on a month-to-month contract."
        )

    if tenure < 12:
        risk_indicators.append(
            "Customer has relatively low tenure."
        )

    if payment_method == "Electronic check":
        risk_indicators.append(
            "Customer uses electronic check for payment."
        )

    if tech_support == "No":
        risk_indicators.append(
            "Customer does not have Tech Support."
        )

    if online_security == "No":
        risk_indicators.append(
            "Customer does not have Online Security."
        )

    if risk_indicators:
        for indicator in risk_indicators:
            st.warning(f"• {indicator}")
    else:
        st.success(
            "No major risk indicators found from the selected inputs."
        )