import streamlit as st
st.title('Hello all')
st.header('my first app')
st.balloons()
x=st.radio('Are you a student',options=['Yes','No'])
if x=='Yes':
    st.write('Student')
else:
    st.write('No I am not a student')    
c1,c2,c3=st.columns(3)    
with c1:
    st.write('India')
    score=400
    st.write(400)
with c2:
    st.write('Aus')
    score=345
    if score<400:
        st.write('Lost')
with c3:
    st.write('India won the cup')    
st.sidebar.markdown('One day')  
st.sidebar.radio('Results',options=['India','Aus'])      