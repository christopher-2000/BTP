import streamlit as st
from pandas import read_csv
from operations import*
data = read_csv("data/cf_data.csv")

def recommend(val):
    st.text("Recommended List of Colleges")
    univs = set(data["univName"])
    rowList = [list(row) for row in data.values]
    
    for i in range(20):
        sim = cosine_sim(val,rowList[i][1:5])
        st.text("{}. {} {}".format(i,rowList[i][5],sim)) 
        
