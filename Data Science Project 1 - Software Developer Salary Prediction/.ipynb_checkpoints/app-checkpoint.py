# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:10:40 2022

@author: Thobela Sixpence
"""

# import libraries
import streamlit as st
from predict_page import show_predict_page
from explore_page import explore_page_show
 
 
explore_page_show()
# create the side bar
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    explore_page_show()

