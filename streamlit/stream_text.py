import streamlit as st

st.title(anchor=None, body="Stream Input Text")
user_input = st.text_area(value=" ", label="input")
if st.button("Stream"):
    st.write_stream("Please implement the stream functionality")
