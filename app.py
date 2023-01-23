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
    st.markdown("<h3 style='text-align: center; color: grey;'>Asep Muhidin  👋</h1>", unsafe_allow_html=True) 

st.write("""
# NLP Preprocessing
Aplikasi pre-processing pada ***NLP (Natural Languange Processing)***
""")

case_folding=st.checkbox("Case Folding")
tokenizer=st.checkbox("Tokenizing")

def CF(teks):
     return teks.lower()

if case_folding:
     st.write("""### Case Folding""")
     st.write("""
     Case Folding adalah proses perubahan huruf kapital menjadi huruf kecil. 
     Tujuannya yaitu kata-kata yang sama tidak terdeteksi berbeda hanya karena perbedaan terdapat huruf kapital.""")
         
     txt_cf=st.text_area("""**Masukkan sembarang teks/paragraph**""",max_chars=200, height=150)
     if st.button('''***Case Folding***''',type='primary'):
          code = '''def CF(teks):
    return teks.lower()'''
          st.code(code, language='python')
          st.success("OUTPUT : " + CF(txt_cf))
          
elif tokenizer:
  st.write("""### Tkenizing""")
  st.write("""
  Tokenizing merupakan proses memisahkan atau memecahkan yang awalnya berupa kalimat menjadi kata-kata atau memutus urutan string 
  menjadi potongan-potongan seperti kata-kata berdasarkan tiap kata yang menyusunnya (Asiyah & Fithriasari, 2016).""")
