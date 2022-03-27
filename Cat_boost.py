import pandas as pd
import streamlit as st
from operations import*
import catboost as cat
import pickle

cat_model = cat.CatBoostClassifier(task_type='CPU', iterations=50, 
                              random_state = 2021, 
                              eval_metric="Accuracy")
cat_model.load_model('data/cat_boost.json')
dataset = pd.read_csv('data/data_classify2.csv')

def cat_recommend(data,fav):
    test = []
    print(data)
    data[0] = (data[0] - min(dataset['greV']))/ (max(dataset['greV']) - min(dataset['greV'])) 
    data[1] = (data[1]- min(dataset['greQ']))/(max(dataset['greQ'])- min(dataset['greQ'])) 
    data[2] = (data[2]- min(dataset['greA']))/(max(dataset['greA'])- min(dataset['greA']))
    data[3] = (data[3]- min(dataset['cgpa']))/(max(dataset['cgpa'])- min(dataset['cgpa']))

    temp = data
    for i in dataset['university'].unique():
        test.append(temp + [i])
    results = pd.DataFrame(cat_model.predict_proba(test),columns=['Reject','Accept'])
    results = pd.concat([pd.DataFrame(dataset['university'].unique(),columns=['university']), results],axis=1)
    
    acc_chance = results.sort_values('Accept')[:10]
    rej_chance = results.sort_values('Reject')[:10]
    st.write("Universities with Lowest chance of Acceptance")
    st.write(drawGraph(acc_chance,'Accept','university','Accept'))

    st.write("Universities with Highest chance of Acceptance")
    st.write(drawGraph(rej_chance,'Accept','university','Accept'))
    
    fav_chance = results[results['university']==fav]['Accept'].values[0]
    st.write("Chance of Acceptance into the dream college ({}): {:.2f}%".format(fav,fav_chance*100))



    pass
