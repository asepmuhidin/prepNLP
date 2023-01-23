import streamlit as st

st.set_page_config(
     page_title="PrepNLP",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

st.write("""
# Preprosesing NLP
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")
