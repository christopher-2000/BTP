import streamlit as st
from options import *
from CF import *
from CBF import *
from Cat_boost import *
from hybrid import*
from pandas import read_csv
from sess import SessionState

data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def sidebar():
    
    name = st.sidebar.text_input(
        'Enter your name')

    dream_col = st.sidebar.selectbox(
        'Choose your dream college',
        data["Institution Name"][2:])

    cgpa = st.sidebar.number_input(
        'Enter your CGPA(Out of 4)',1.0
    )
    st.sidebar.text(
        'Enter your GRE scores'
    )
    greV = st.sidebar.number_input(
        'greV(Out of 170)',130.0
    )
    greQ = st.sidebar.number_input(
        'greQ(Out of 170)',130.0
    )

    greA = st.sidebar.number_input(
        'greA(Out of 6)',1.0
    )

    rec_button = st.sidebar.empty()
    ss = SessionState.get(rec_button = False)

    if rec_button.button('Recommend Universities'):
        ss.rec_button = True

    if ss.rec_button:
        st.success("Hey "+ name +", Choose Your Method for recommendation")  
        choice = st.radio(
            "", 
            ('Collaborative Filtering','Content based Filtering','Hybrid','Neural Network','Cat Boost')
            )  
        
        if st.button("Recommend") is True:
            if choice=='Collaborative Filtering':
                cf_recommend([greV,greQ,greA,cgpa],algo='cosine')

            if choice =='Content based Filtering':
                cbf_recommend(dream_col)
            if choice=='Hybrid':
                hybrid_recommend([greV,greQ,greA,cgpa])
            if choice=='Neural Network':
                hybrid_recommend([greV,greQ,greA,cgpa])
            if choice=='Cat Boost':
                cat_recommend([greV,greQ,greA,cgpa],dream_col)
'''
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
'''