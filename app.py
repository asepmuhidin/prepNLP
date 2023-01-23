import streamlit as st
from PIL import Imgae

st.set_page_config(
     page_title="PrepNLP",
     layout="centered"
 )

image=Image.open("images/photok.jpg")

with st.sidebar:
    st.image(image, width=120)

st.write("""
# Preprosesing NLP
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")
