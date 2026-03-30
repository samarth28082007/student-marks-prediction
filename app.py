import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

st.title("Student Marks Prediction")

hours = st.number_input("Enter study hours")

if st.button("Predict"):
    input_data = pd.DataFrame([[hours]], columns=['hours'])
    prediction = model.predict(input_data)
    st.success(f"Predicted Marks: {prediction[0]:.2f}")