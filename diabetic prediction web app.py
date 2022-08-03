# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:44:25 2022

@author: PURUSHOTHAM
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('D:/diabetic prediction deployment/trained_model.sav','rb'))

#creating function for prediction:
    
def diabetes_prediction(input_data):
    # input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    
    #giving a title for web page
    st.title('Diabetes Prediction by Nivedhitha')
    
    #creating inputs - 8 inputs
    #from the user
    
    Pregnancies = st.text_input('Enter Number of Pregnancies')
    Glucose= st.text_input('Enter Glucose level')
    BloodPressure= st.text_input('Enter bloodpressure')
    SkinThickness = st.text_input('Enter Skin thickness')
    Insulin = st.text_input('Enter Number of Insulin')
    BMI = st.text_input('Enter BMI')
    DiabetesPedigreeFunction = st.text_input('Enter DiabetesPedigreeFunction')
    Age = st.text_input('Enter Age')
    
    #code for prediction
    
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Diabetic Test result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    #printing the result
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    