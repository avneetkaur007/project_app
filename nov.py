import streamlit as st
st.balloons()
x=st.radio('Are you a student',options=['Yes','NO'])
if x=='Yes':
    st.write('Yes ,I am a student')
else:
    st.write('No ,I am not a student')    

c1,c2,c3=st.columns(3)
with c1:
    st.write('India')
    y=int(st.text_input(''))
    z=y*10
    if z>=10000:
        st.write('hello')
with c2:
    st.write('New delhi')
with c3:
    st.write('Noida')        
a=st.text_input('Enter your percentage')    
st.sidebar.markdown('test')
b=st.slider('slider for ages')
if b<20:
    st.write('Young')

st.text_input('Enter your name') 
m=st.text_input('marks')  
tm=st.text_input('total marks')
per=(int(m)/int(tm))*100
if per>=75:
    st.write('Eligible')
else:
    st.write('Not elegible')    
