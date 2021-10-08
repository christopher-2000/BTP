from pandas import read_csv
import streamlit as st
import time
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')
shiksha_data = read_csv("data/display_data.csv")

def display_college(college):
    entry = data[data['Institution Name'] == college].values[0]
    cols = [i for i in data]
    for i,j in zip(entry,cols):
        st.write(j+" : "+str(i))
    
    if college in shiksha_data['college'].values:
        shiksha_entry = shiksha_data[shiksha_data['college']==college].values[0]
        for i in shiksha_entry:
            st.text(" ".join([p for p in str(i).split(" ") if p!='' and p!='\n']))


        