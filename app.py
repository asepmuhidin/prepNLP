import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="PrepNLP",
     layout="centered"
 )

image=Image.open("images/photok.jpg")

with st.sidebar:
    st.image(image, width=120, caption='Asep Muhidin')


st.write("""
# Preprosesing NLP
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")
