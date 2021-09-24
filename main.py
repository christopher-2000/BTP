import streamlit as st
from options import *
st.write("""
# University Recommendation System
### Btech Project 
""")
name = st.sidebar.text_input(
    'Enter your name')

col_type = st.sidebar.selectbox(
    'Choose the type of college',
    COL_TYPES)

cgpa = st.sidebar.number_input(
    'Enter your CGPA'
)
st.sidebar.text(
    'Enter your GRE scores'
)
grev = st.sidebar.number_input(
    'greV'
)
grep = st.sidebar.number_input(
    'greV'
)

