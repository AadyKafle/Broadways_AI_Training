import streamlit as st
import joblib
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)

petal_length = st.number_input('enter petal length')
petal_width = st.number_input('enter petal width')
sepal_length = st.number_input('enter sepal length')
sepal_width = st.number_input('enter sepal length')

flower_btn = st.button('predict flower')

loaded_model = joblib.load('iris_classifier_knn.joblib')

sample = [[sepal_length,sepal_width,petal_length,petal_width]]
pred = loaded_model.predict(sample)[0]

# st.write(f'your flower is {iris.target_names[pred]}')

if flower_btn:
    st.write(f'your flower is {iris.target_names[pred]}')