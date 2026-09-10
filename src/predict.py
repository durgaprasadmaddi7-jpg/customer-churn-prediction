import joblib
import pandas as pd


# Load trained model
MODEL_PATH = "models/customer_churn_model.pkl"

model = joblib.load(MODEL_PATH)

# Final threshold selected during model evaluation
FINAL_THRESHOLD = 0.40


def predict_churn(customer_data):
    """
    Predict whether a customer is likely to churn.

    Parameters:
        customer_data (dict): Customer information

    Returns:
        probability (float): Churn probability
        prediction (int): 0 = No Churn, 1 = Churn
    """

    # Convert dictionary into DataFrame
    customer_df = pd.DataFrame([customer_data])

    # Get churn probability
    probability = model.predict_proba(customer_df)[0, 1]

    # Apply final threshold
    prediction = int(probability >= FINAL_THRESHOLD)

    return probability, prediction

if __name__ == "__main__":

    test_customer = {
        'gender': 'Male',
        'SeniorCitizen': 0,
        'Partner': 'Yes',
        'Dependents': 'No',
        'tenure': 12,
        'PhoneService': 'Yes',
        'MultipleLines': 'No',
        'InternetService': 'Fiber optic',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'Yes',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'Yes',
        'StreamingMovies': 'No',
        'Contract': 'Month-to-month',
        'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check',
        'MonthlyCharges': 75.50,
        'TotalCharges': 906.00
    }

    probability, prediction = predict_churn(test_customer)

    print(f"Churn Probability: {probability:.3f}")
    print(f"Prediction: {prediction}")

    if prediction == 1:
        print("Result: Customer is likely to churn")
    else:
        print("Result: Customer is likely to stay")