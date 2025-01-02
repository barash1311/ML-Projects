import streamlit as st

st.title("streamlit text input")
name=st.text_input("enter your name")


age=st.slider("slect your age:",0,100,25)
st.write(f"your age is {age}")
options=["python","java","c++","javascript"]
choice=st.selectbox("choose youe lang:",options)
st.write(f'you selected {choice}')

if name:
    st.write(f"hello,{name}")
    
uploaded=st.file_uploader("choose a csv file",type="csv")