import streamlit as st
from options import *
from CF import *
from CBF import *
from pandas import read_csv
from sess import SessionState

data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def sidebar():
    
    name = st.sidebar.text_input(
        'Enter your name')

    dream_col = st.sidebar.selectbox(
        'Choose your dream college',
        data["Institution Name"])

    cgpa = st.sidebar.number_input(
        'Enter your CGPA'
    )
    st.sidebar.text(
        'Enter your GRE scores'
    )
    greV = st.sidebar.number_input(
        'greV'
    )
    greQ = st.sidebar.number_input(
        'greQ'
    )

    greA = st.sidebar.number_input(
        'greA'
    )

    rec_button = st.sidebar.empty()
    ss = SessionState.get(rec_button = False)

    if rec_button.button('Recommend Universities'):
        ss.rec_button = True

    if ss.rec_button:
        st.write("Choose Your Method for recommendation")  
        if st.button('Collaborative Filtering') is True:
            cf_recommend([greV,greQ,greA,cgpa])
        if st.button('Content based Filtering') is True:
            cbf_recommend(dream_col)
        if st.button('Hybrid') is True:
            hybrid_recommend([greV,greQ,greA,cgpa])
        
def trial():
    button1 = st.empty()
    text1 = st.empty()
    button2 = st.empty()
    text2 = st.empty()

    ss = SessionState.get(button1 = False)

    if button1.button('1') :
        ss.button1 = True

    if ss.button1:
        text1.write('you clicked the first button')
        if button2.button('2'):
            text2.write('you clicked the second button')