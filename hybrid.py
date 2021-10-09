import streamlit as st
from pandas import read_csv
from operations import*
from CF import *
from CBF import *
data = read_csv("data/cf_data.csv")

def hybrid_recommend(val):
    st.markdown("Recommended List of Colleges using Hybrid filtering")
    cols = cf_recommend(val,False)
    i = 0
    while True:
        first = cols[i]
        try:
            cbf_recommend(first[1],False)
            break
        except:
            i+=1

    
        
