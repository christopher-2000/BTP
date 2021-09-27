from pandas import read_csv
import streamlit as st

from pandas import read_csv
import streamlit as st
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def display_top():
    st.markdown("Top 5 Universites according to QS world rankings")
    for i in range(5):
        st.text("{}. {} {}".format(i+1,data["Institution Name"][i],data["Overall Score"][i]))