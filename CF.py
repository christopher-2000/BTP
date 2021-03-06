from pandas import read_csv
from pandas import DataFrame
import plotly.express as px
import streamlit as st
from operations import*
data = read_csv("data/cf_data.csv")

def display_cfhead():
    st.dataframe(data.head())

def cf_recommend(val,flag=True,algo='cosine'):
    #st.text("Recommended List of Colleges")
    if val == [0,0,0,0]:
        return st.markdown("Please Enter Valid Scores")
    
    rowList = [list(row) for row in data.values]
    colleges = []
    for i in range(len(rowList)):
        # Similarity Finding
        if algo=='cosine':
            sim = cosine_sim(val,rowList[i][1:5])
        else:
            sim = euclidean(val,rowList[i][1:5])
        colleges.append([sim,rowList[i][5]])
        
    #sorted list of colleges
    check = set()
    colleges_sorted = sorted(colleges,key = lambda x: x[0])[::-1]
    final_cols = []
    n = 0
    
    while n<len(colleges_sorted):
        if colleges_sorted[n][1] not in check:
            final_cols.append(colleges_sorted[n])
            check.add(colleges_sorted[n][1])
        n+=1

    if flag:
        st.markdown("Recommended List of Colleges using Collaborative filtering")
        col = []
        for i in range(10):
            col = [[str(i+1)+" ." + final_cols[i][1]+" ",final_cols[i][0]]] + col
            #st.text("{}. {} {}".format(i+1,fin_20[i][1],fin_20[i][0])) 
        vals = DataFrame(col,columns=['University','Score'])
        vals['Score'] = vals['Score']*100
        st.write(drawGraph(vals,'Score','University','Score'))
    else:
        return final_cols
    
    
