import streamlit as st
from pandas import read_csv
from operations import*
from CF import *
data = read_csv("data/cf_data.csv")

def hybrid_recommend(val):
    st.markdown("Recommended List of Colleges using Hybrid filtering")
    st.text("Work in Progress")
        
