%%writefile app.py

import streamlit as st
import joblib
model = joblib.load('CUSTOMERID-SPENDINDSCORE')
st.title("CUSTOMERID-SPENDINDSCORE")
ip = st.text_input('Enter the customerid:')
op = model.predict([ip])
if st.button('enter'):
  st.title(op[0])
