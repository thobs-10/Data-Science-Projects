# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 01:30:51 2022

@author: Thobela Sixpence
"""

# import libraries
import streamlit as st
import pickle
import numpy as np

# we need to load the model for prediction
def load_model():
    with open(r'C:\Users\Cash Crusaders\Desktop\My Portfolio\Projects\Data Science Projects\Data Science Project 1 - Software Developer Salary Prediction\saved_model.h5', 'rb') as file:
        saved_model = pickle.load(file)
    return saved_model

saved_model = load_model()

# get the necessaru libraries required for data transformation
regressor = saved_model["regressor"]
le_country = saved_model["le_country"]
le_education = saved_model["le_education"]

# create the page for predict with its UI
def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")
    
    # all the countries in the datasset with more or equal to the cutoff value
    
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )
    
     
    # education qualifications
    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )
      
    # create a dropdown sselector for countries and education
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    
    # a slider for experience
    expericence = st.slider("Years of Experience", 0, 20, 3)
    
    # create a button for prediction
    ok = st.button("Calculate Salary")
    if ok:
        # encode the categorical values
        input_x = np.array([[country, education, expericence]])
        input_x[:,0] = le_country.transform(input_x[:,0])
        input_x[:,1] = le_education.transform(input_x[:,1])
        input_x = input_x.astype(float)
        
        # predict
        
        salary = regressor.predict(input_x)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")


