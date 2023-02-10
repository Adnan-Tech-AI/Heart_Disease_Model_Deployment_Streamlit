import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import joblib



    
st.markdown("<h2 style='text-align:center;font-weight:bold;font-family:Lora;'>Heart Disease Prediction Model</h2>",unsafe_allow_html=True)

gender = st.radio("Enter Your Gender",["Male","Female"])
age =st.slider("Enter Your Age",min_value=1,max_value=100)
currentSmoker = st.radio("Are you a smoker",["No","Yes"])
if currentSmoker=="Yes":
    cigsPerDay=st.number_input("How Many ciggarettes per day",step=1) or 0
BPMeds=st.radio("Do you take BP Medicines",["Yes","No"])
prevalentStroke=st.radio("Do you have any prevalent stroke",["Yes","No"])
prevalentHyp=st.radio("Do you have any prevalent Hypertension",["Yes","No"])
diabetes=st.radio("Do you have diabetes",["Yes","No"])
totChol=st.number_input("What is Your cholestrol level",step=1)
sysBP=st.number_input("What is Your sysBP level",step=1)
diaBP=st.number_input("What is Your diaBP level",step=1)
BMI=st.number_input("What is Your BMI level",step=1)
heartRate=st.number_input("Enter Your Heart Beats Per Minute",step=1)

if gender=="Male":
    sex=1
else:
    sex=0

if currentSmoker=="Yes":
    smoke=1
else:
    smoke=0

if BPMeds=="Yes":
    BPMedicine=1
else:
    BPMedicine=0

if prevalentStroke=="Yes":
    prevStroke=1
else:
    prevStroke=0

if diabetes=="Yes":
    diab=1
else:
    diab=0

if prevalentHyp=="Yes":
    prevHyp=1
else:
    prevHyp=0


if st.button("Predict"):

        X=[[sex,age,smoke,cigsPerDay,BPMedicine,prevStroke,prevHyp,diab,totChol,sysBP,diaBP,BMI,heartRate]]
        model = joblib.load("model.h5")
        prediction=model.predict(X)
        if prediction==[0]:
            st.success("The patient is not at risk of heart disease")
        else:
            st.success("The patient is at risk of heart disease in next ten years, we suggest to make lifestyle changes")

