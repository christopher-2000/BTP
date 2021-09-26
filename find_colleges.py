import streamlit as st
from pandas import read_csv
data = read_csv("data/cf_data.csv")

def recommend():
    st.text("Recommended List of Colleges")
    univs = set(data["univName"])
    c = 1
    for i in univs:
        st.text("{}. {}".format(c,i))
        c+=1
