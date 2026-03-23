import streamlit as st
import pandas as pd
import numpy as np 

st.title("Hello GeeksForGeeks !!!")

df = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 25]
})

st.dataframe(df)   # interactive
st.table(df) 

