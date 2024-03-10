import pickle
import streamlit as st
import pandas as pd


df= pd.read_csv("cars24-car-price.csv")

st.header("Car Price Prediction Application")

col1, col2 = st.columns(2)

with col1:
    f1=st.selectbox(
        'Select the fuel type',
        ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))
with col2:
    engine=st.slider(
        'Engine power',
        500, 5000, step=100)


col1, col2 = st.columns(2)

with col1:
    t1=st.selectbox(
        'Select the transmission',
        ('Manual','Automatic' ))
with col2:
    seats = st.selectbox(
        'Select the number of seats',
        [4,5,6,7,9,11])


encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

def model_pred(fuel_type, engine, transmission, seats):
    input_features=[[2012.0,1, 120000, fuel_type, transmission,19.7,engine,46.3,seats]]

    with open("car_pred", 'rb') as file:
        reg_model=pickle.load(file)

    return reg_model.predict(input_features)



if st.button('Predict'):
    #encoding of all categorical var according to encode dict
    fuel_type= encode_dict['fuel_type'][f1]
    transmission_type= encode_dict['transmission_type'][t1]

    pred= model_pred(fuel_type, engine,transmission_type, seats )

    st.text("Predicted price of the carr is: " + str(pred.round(4)))



