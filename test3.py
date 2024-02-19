import streamlit as st
st.sidebar.markdown('Test')
st.text_input('Company name')
st.sidebar.radio('No. of Projects',options=['1','2','3'])
st.sidebar.text_input('Manager name')
st.balloons()
v=st.slider('How old are you',0,100)
st.write(v)
