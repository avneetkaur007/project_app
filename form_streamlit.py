import streamlit as st
with st.form('form'):
    st.write('Please fill the form')
    name=st.text_input('Name')
    college_name=st.text_input('Your college name')
    Percentage=st.number_input('Your Percentage')
    Working=st.checkbox('Are you working')

    submitted=st.form_submit_button('Submit')
    st.write('name:',name)
    st.write('college_name:',college_name)
    st.write('Percentage:',Percentage)
    st.write('Are you working',Working)