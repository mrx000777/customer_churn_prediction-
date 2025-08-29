import streamlit as st
import numpy as np
import joblib

st.title("Customer Churn Prediction App")
st.divider()
st.write("Please enter the values and press the Predict button")
st.divider()

age = st.number_input("Enter the Age ", min_value=10, max_value=100, value=30)
tenure = st.number_input("Enter the Tenure", min_value=0, max_value=130, value=10)
monthlycharges = st.number_input("Enter the Monthly Charges ", min_value=30, max_value=150, value=70)
gender = st.selectbox("Enter the Gender ", ["Male", "Female"])
st.divider()
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

predictbutton = st.button("Predict!")
st.divider()

if predictbutton:
    gender_selected = 1 if gender == "Female" else 0
    x = [age, gender_selected, tenure, monthlycharges]
    x_array = scaler.transform([np.array(x)])


    prediction = model.predict(x_array)[0]
    predicted = "Churn: YES" if prediction == 1 else "Churn: NO"


    probas = model.predict_proba(x_array)[0]  # [prob_No, prob_Yes]

    st.balloons()
    st.success(f" Prediction: **{predicted}**")
    st.info(f" Probability of NO churn: {probas[0]*100:.2f}%")
    st.warning(f" Probability of YES churn: {probas[1]*100:.2f}%")

else:
    st.write("Please enter the values and press the Predict button")
