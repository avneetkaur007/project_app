import streamlit as st
st.title('Bank Name')
st.write('Check your eligibility')
sal=st.number_input('Enter your salary')
st.number_input('Enter Loan amount you are applying')
st.button('Submit')
if sal<50000:
    st.write('Sorry you are not eligible')
else:
    st.write('Congratulations')
    st.balloons()