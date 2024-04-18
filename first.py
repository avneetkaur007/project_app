import streamlit as st
st.title('Hello python')
st.write('this is out first app on streamlit')
#st.balloons()

x=st.radio('Are you a student',options=['Yes','No'])
if x=='Yes':
    st.write('Great')
else:
    st.write('okay')
name=st.text_input('What is your name')
st.number_input('Enter your percentage')
st.sidebar.markdown('Test results')
a=st.sidebar.checkbox('Are you working')
if a==1:
    st.sidebar.write('Great')
income=st.number_input('Enter your income')
st.button("check eligibility")
if income >30000 :
    st.success(f"congratulations! {name} is eligible for the loan.")
else:
    st.error(f"sorry ,{name} is not eligible for the loan.")