import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.header('Hello to my first app!')
st.header('Swapnil is :blue[cool] :sunglasses:')


st.write(df)

def square(num):
  return num*num

number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.write (" Result is ", square(number))