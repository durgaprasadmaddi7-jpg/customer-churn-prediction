# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a customer is likely to churn.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model training, model evaluation, and an interactive Streamlit dashboard for customer churn prediction.

---

## 📌 Project Overview

Customer churn occurs when a customer stops using a company's services.

The goal of this project is to use customer information such as:

- Customer demographics
- Tenure
- Internet service
- Contract type
- Payment method
- Monthly charges
- Total charges
- Support services

to predict the probability that a customer will churn.

---

## 🔄 Project Workflow

```text
Raw Customer Data
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Data Preprocessing
        ↓
Model Training
        ↓
Model Comparison
        ↓
Random Forest Hyperparameter Tuning
        ↓
Threshold Tuning
        ↓
Final Model
        ↓
Streamlit Dashboard
        ↓
Customer Churn Prediction

----

## 📊 Dashboard Examples

The project includes an interactive Streamlit dashboard that predicts customer churn probability and displays the customer's risk level.

### 🟢 Low Risk

![Low Risk](screenshots/low-risk.png)

### 🟡 Medium Risk

![Medium Risk](screenshots/medium-risk.png)

### 🔴 High Risk

![High Risk](screenshots/high-risk.png)

---

## 📈 Model Performance

The final Random Forest model was evaluated using the following metrics:

| Metric | Score |
|---|---:|
| Accuracy | 78.4% |
| Precision | 58.5% |
| Recall | 64.7% |
| F1 Score | 61.4% |
| ROC-AUC | 84.4% |

The final churn classification threshold was set to **0.40** to improve the balance between identifying customers likely to churn and avoiding unnecessary false predictions.

---

## 🌲 Final Model

The final model used in this project is a **Random Forest Classifier**.

### Hyperparameters

```text
n_estimators = 200
max_depth = 10
min_samples_split = 2
min_samples_leaf = 2
random_state = 42
---

## 🧠 Model Development

Several machine learning models were evaluated during the project, including:

- Logistic Regression
- Decision Tree
- Random Forest

Random Forest achieved the best overall performance based on ROC-AUC and was selected as the final model.

---

## 🎯 Final Prediction Threshold

The default classification threshold was initially 0.50.

After threshold analysis, a threshold of **0.40** was selected for the final model.

This threshold helps identify more customers who are likely to churn while maintaining a reasonable balance between precision and recall.

The dashboard uses this threshold to classify customers into churn or non-churn predictions.

---

## 🌐 Streamlit Dashboard

An interactive Streamlit dashboard was developed to allow users to enter customer information and receive a churn prediction.

The dashboard provides:

- Customer information input
- Service information input
- Contract and billing information
- Churn probability
- Risk level
- Risk indicators
- Final churn prediction

### Risk Levels

| Churn Probability | Risk Level |
|---|---|
| Below 30% | 🟢 Low Risk |
| 30% – 60% | 🟡 Medium Risk |
| Above 60% | 🔴 High Risk |

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── raw/
│       └── Telco-Customer-Churn (2).csv
│
├── models/
│   └── customer_churn_model.pkl
│
├── notebooks/
│   ├── 1_data_understanding.ipynb
│   ├── Data_cleaning.ipynb
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   └── Model_Building.ipynb
│
├── screenshots/
│   ├── low-risk.png
│   ├── medium-risk.png
│   └── high-risk.png
│
├── src/
│   └── predict.py
│
├── .gitignore
├── README.md
└── requirements.txt

Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Matplotlib
Seaborn
Jupyter Notebook
Streamlit
Git
GitHub