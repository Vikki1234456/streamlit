import streamlit as st
import pandas as pd

st.write("""
# App To Find Largest Number Among Given 3 Numbers
""")

st.header('User Input Parameters')

def user_input_features():
    number1 = st.number_input("no1", min_value=-3000, max_value=200000000)
    number2 = st.number_input("no2", min_value=-3000, max_value=200000000)
    number3 = st.number_input("no3", min_value=-3000, max_value=200000000)

    data = {
        'number1': number1,
        'number2': number2,
        'number3': number3
    }

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df.to_dict())

def maxi(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
    
max_val = maxi(df['number1'][0], df['number2'][0], df['number3'][0])
st.subheader('Largest Number Among the 3 Numbers')
st.write(max_val)  # Maximum value
