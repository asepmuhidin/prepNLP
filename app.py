import streamlit as st

st.set_page_config(
     page_title="PrepNLP",
     layout="centered"
 )
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

st.write("""
# Preprosesing NLP
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")
