import re
from pandas import read_csv
import streamlit as st
from college_view import*

data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def display_top():
    st.write("""
    ## Top 5 Universites according to QS world rankings 2020
    """)
    for i in range(1,6):
        st.markdown("{}. {} {}".format(i,data["Institution Name"][i],data["Overall Score"][i]))

def search_college():
    college = st.selectbox('Search for a college',data["Institution Name"])
    region = st.selectbox('Search for a region',data["Region"].unique())
    if st.button('Search now'):
        if college=='NONE' and region!='NONE':
            display_regionwise(region)
        else:
            display_college(college)

