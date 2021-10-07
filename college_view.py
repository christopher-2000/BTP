from pandas import read_csv
import streamlit as st
import time
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')


def display_college(college):
    entry = data[data['Institution Name'] == college].values[0]
    cols = [i for i in data]
    for i,j in zip(entry,cols):
        st.write(j+" : "+str(i))


        