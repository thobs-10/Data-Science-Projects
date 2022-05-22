# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:37:49 2022

@author: Cash Crusaders
"""

import numpy as np
import pickle 


# Loading the saved model
loaded_model = pickle.load(open('C:/Users/Cash Crusaders/Desktop/My Portfolio/Projects/Data Science Projects/Classification/Diabetes Prediction/trained_model.sav', 'rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the data into a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


# prediction using the model
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0]==0:
    print('The person is not diabetic')
else:
    print('The person is diabetic')
    

