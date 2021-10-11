from pandas import read_csv,DataFrame
import streamlit as st
import time
from operations import*
from annotated_text import annotated_text

data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')
shiksha_data = read_csv("data/display_data.csv")

def display_college(college):
    entry = data[data['Institution Name'] == college].values[0]
    cols = [i for i in data]

    dis={}
    for i,j in zip(entry[:8],cols[:8]):
        dis[j]=str(i)
    abbrev = { 'VH': 'Very High', 'HI': 'High', 'MD': 'Medium', 'LO': 'Low'}

    st.markdown("### **{}**".format(dis['Institution Name']))
    st.markdown("##### {}".format(dis['Unnamed: 2']))
    st.markdown("##### Rank in 2020: #{} ".format(dis['Rank in 2020']))
    annotated_text(
        ('AGE' + " : "+dis['AGE'],"","#fca311","#000"),
        "  ",
        ('RESEARCH INTENSITY' + " : "+ abbrev[dis['RESEARCH INTENSITY']],"","#d62828","fff"),
        "  ",
        (dis['STATUS']+ " - "+ 'University',"","#8ef","#000")
        
    )
    req=cols[8:]
    df=[]

    for i,j in zip(req,entry[8:]):
        df.append([i,type_change(j)])

    graph=DataFrame(df,columns=['metric','score'])    
    st.write(drawGraph(graph,'score','metric'))

    if college in shiksha_data['college'].values:
        shiksha_entry = shiksha_data[shiksha_data['college']==college].values[0]
        for i in shiksha_entry:
            st.text(" ".join([p for p in str(i).split(" ") if p!='' and p!='\n']))
    
    


        