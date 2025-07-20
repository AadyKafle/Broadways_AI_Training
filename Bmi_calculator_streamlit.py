import streamlit as st
st.header('BMI calculator')

weight = st.number_input('enter your weight in KGs')
height = st.number_input('enter your height in feet')


bmi_btn =st.button('show BMI')


if bmi_btn:

    bmi = weight/((height/3.28)**2)

    if bmi<16:
        st.error('Extremely Underweight!, How are you even alive')
    elif bmi>=16 and bmi<18.5:
        st.warning('Underweight Eat something Brother')
    elif bmi>=18.5 and bmi<25:
        st.success('Healthy guy HUH , keep it up')
    elif bmi>=25 and bmi<30:
        st.info('Overweight, fatso! do some cardio')
    elif bmi>=30:
        st.error('Extremely Overweight, You are the reason earth slowed its rotation speed')