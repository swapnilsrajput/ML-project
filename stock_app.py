import streamlit as st
import yfinance as yf
import datetime


txt= st.text_input("Enter the stock")
msft = yf.Ticker(txt)

st.write(msft)

st.header("Welcome to Stock Analysis")
# get historical market data

col1, col2 = st.columns(2)
with col1:
    sd = st.date_input("Start Date",  datetime.date(2019, 7, 6))
with col2:
    ed = st.date_input("End Date")

hist = msft.history(period="1d", start=sd,
                                       end=ed)

st.dataframe(hist)

st.subheader("DAILY CLOSING CHART")
st.line_chart(hist['Close'])

st.subheader("DAILY VOLUME TRADE CHART")
st.line_chart(hist['Volume'])