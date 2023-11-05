import streamlit as st
st.title('Our first application')
st.header('Lets start')
st.balloons()
st.text_input('Name')     

c1,c2,c3=st.columns(3)
with c1  :
    st.write('India')  
    st.write(300)
with c2:
    st.write('SA')
    st.write(256)
with c3:
    st.write('Result')   
    st.write('India won') 
st.sidebar.markdown('Test')    
x1=st.sidebar.radio('are you a student',options=['yes','No'],index=0) 
if  x1=='yes':
    st.write('student')  
else:
    st.write('No I am not a student')         