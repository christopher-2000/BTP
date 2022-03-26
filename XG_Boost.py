'''
import streamlit as st
from operations import*
import xgboost as xgb
import pickle

xg_model = xgb.XGBClassifier()
xg_model.load_model("data/xgboost_model.json")

with open('data/univ_id.pickle', 'rb') as handle:
    univ_id = pickle.load(handle)

def xg_recommend(data):
    n = len(univ_id)/2
    test = []
    temp = data[:3] + data[4] + [sum(data[:4]),sum(data[:3])]
    for i in range(n):
        test.append(temp + [i])
    dtest = xgb.DMatrix(test)

    print(xg_model.predict(dtest))

    pass
'''

