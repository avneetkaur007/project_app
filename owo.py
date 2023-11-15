import streamlit as st
st.title('Hello this is my first app')
st.header('second line')
#Radio button
x=st.radio('Are You a Student',options=['Yes','No'],index=0)
if x=='Yes':
    st.write('I am a Student')
else:
    st.write('No i am not a student')    
c1,c2,c3=st.columns(3)
with c1:
    st.write('India')
    if x=='Yes':
        st.write('Hello')
with c2:
    st.write('Delhi')
    if x=='Yes':
        st.write('Hello')
with c3:
    st.write('size') 
    if x=='Yes':
        st.write('BYEEE') 
#side bar
st.sidebar.markdown('Test')    
             