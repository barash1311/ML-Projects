import streamlit as st
import pandas as pd
import numpy as np

#title of the application
st.title("hello streamlit")

##display a  simple text
st.write("this is a simple text")
##create a data frame
df=pd.DataFrame({
    "first column":[1,2,3,4,5],
    "second column":[10,20,30,40,50]
})
##display the data frame
st.write(df)

##create line chart
char_Data=pd.DataFrame(
    np.random.randn(20,4),columns=["a","b","c","d"]
)
st.line_chart(char_Data)

