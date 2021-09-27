import streamlit as st
from pandas import read_csv
from operations import*
from CF import *
data = read_csv("data/cf_data.csv")

def recommend(val):
    st.text("Recommended List of Colleges")
    cf_recommend(val)
        
