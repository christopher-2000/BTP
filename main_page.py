from pandas import read_csv
import streamlit as st

from pandas import read_csv
import streamlit as st
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def display_top():
    st.write("""
    ## Top 5 Universites according to QS world rankings 2020
    """)
    for i in range(5):
        st.markdown("{}. {} {}".format(i+1,data["Institution Name"][i],data["Overall Score"][i]))

def search_college():
    st.selectbox('Search for a college',data["Institution Name"])
    if st.button('Search'):
        pass

