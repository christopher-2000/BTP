from pandas import read_csv
import streamlit as st
from operations import*
data = read_csv("data/cf_data.csv")

def display_cfhead():
    st.dataframe(data.head())

def cf_recommend(val):
    #st.text("Recommended List of Colleges")
    rowList = [list(row) for row in data.values]
    colleges = []
    for i in range(len(rowList)):
        sim = cosine_sim(val,rowList[i][1:5])
        colleges.append([sim,rowList[i][5]])
    check = set()
    colleges_sorted = sorted(colleges,key = lambda x: x[0])[::-1]
    fin_20 = []
    n = 0

    while n<len(colleges_sorted):
        if colleges_sorted[n][1] not in check:
            fin_20.append(colleges_sorted[n])
            check.add(colleges_sorted[n][1])
        n+=1

    for i in range(20):
        st.text("{}. {} {}".format(i+1,fin_20[i][1],fin_20[i][0])) 
        

