import streamlit as st
from pandas import read_csv
from pandas import DataFrame
from math import isnan
from operations import*
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')

def cbf_recommend(val):
    st.markdown("Recommended List of Colleges using Content based filtering")
    rowList = [list(row) for row in data.values]
    curr = data[data["Institution Name"] == val].values[0]

    curr = [type_change(x) for x in curr[8:]]
    colleges = []

    for i in range(len(rowList)):
        f = []
        for x in rowList[i][8:]:
            if isnan(type_change(x)):
                f.append(10)
            else:
                f.append(type_change(x)) 

        #print(f)
        sim = cosine_sim(curr,f)
        colleges.append([sim,rowList[i][1]])

    colleges_sorted = sorted(colleges)[::-1]
    
    col = []
    for i in range(10):
        col = [[str(i+1)+" ." + colleges_sorted[i][1]+" ",colleges_sorted[i][0]]] + col
        #st.text("{}. {} {}".format(i+1,colleges_sorted[i][1],colleges_sorted[i][0])) 
    vals = DataFrame(col,columns=['University','Score'])

    st.write(drawGraph(vals,'Score','University','Score'))
        
    

