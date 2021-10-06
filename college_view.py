from pandas import read_csv
import streamlit as st
import time
data = read_csv("data/cbf_data.csv",encoding='ISO-8859-1')


def display_college(college):
    entry = data[data['Institution Name'] == college]
    for i in entry:
        print(entry[i][0])
        