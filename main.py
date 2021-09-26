import streamlit as st
from options import *
from CF import *
from CBF import *
from find_colleges import*
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
greV = st.sidebar.number_input(
    'greV'
)
greQ = st.sidebar.number_input(
    'greQ'
)

greA = st.sidebar.number_input(
    'greA'
)
if st.sidebar.button('Recommend Universities') is True:
       recommend([greV,greQ,greA,cgpa])
display_top()
