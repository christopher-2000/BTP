from pandas import read_csv
import streamlit as st
data = read_csv("cf_data.csv")

def display_cfhead():
    st.dataframe(data.head())

