import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="PrepNLP",
     layout="centered"
 )

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

image=Image.open("images/photoku.jpg")

with st.sidebar:
    st.image(image, width=120)
    "## Asep Muhidin"  



st.write("""
# Preprosesing NLP
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")
