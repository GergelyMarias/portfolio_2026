import streamlit as st

st.set_page_config(page_title="My First App", layout="centered")

st.title("My First Streamlit App")

number_1 = 42
number_2 = 7
number_3 = 128

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Number 1", number_1)

with col2:
    st.metric("Number 2", number_2)

with col3:
    st.metric("Number 3", number_3)
