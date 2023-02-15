import streamlit as st
st.sidebar.markdown('Test')
x=st.sidebar.radio('Are you a student',options=['Yes','No'])
if (x=='Yes'):
    st.write('student')
else:
    st.write('No I am not a Student')
col1,col2,col3=st.columns(3)
with col1:
    st.write('India')
with col2:
    st.write('Delhi')
with col3:
    st.write('Noida')
with st.expander('Comment'):
    comment=st.text_area('',placeholder='Enter a comment here...')
