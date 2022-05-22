# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:48:36 2022

@author: Cash Crusaders
"""

import numpy as np
import pickle
import streamlit as st


# Loading the saved model
loaded_model = pickle.load(open('C:/Users/Cash Crusaders/Desktop/My Portfolio/Projects/Data Science Projects/Classification/Diabetes Prediction/trained_model.sav', 'rb'))

# create function for prediction
def diabetes_prediction(input_data):
    
    

    # changing the data into a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    
    # prediction using the model
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if prediction[0]==0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    

# using the streamlit library

def main():
    
    # title for wep app
    st.title('Diabetes Prediction Wep App')
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of person')
    
    
    # code for prediction
    diagnosis = ""
    
    # creating a button for prediction
    if st.button('Daibetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    
    st.success(diagnosis)
    


    

if __name__ == '__main__':
    main()
    
    
    
