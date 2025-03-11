# import library
import streamlit as st
import eda
import prediction

with st.sidebar:
    st.title('Navigation')
    navigation = st.selectbox('Page', ['Summary', 'Predict Reviews'])

    st.write('___')
    st.title('About')
    st.write('This project is used to predict the sentiment analysis (positive or negative) of reviews.')

if navigation == 'Summary':
    eda.run()
else:
    prediction.run()


