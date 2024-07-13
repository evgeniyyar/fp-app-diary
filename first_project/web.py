import streamlit as st
import functions


todos = functions.read_todos()

st.title("My todo App")
st.subheader("Подзаголовок")
st.write("Какой-то текст")

for index in todos:
    st.checkbox(index)
