import streamlit as st
from PIL import Image

st.title('Web App')
st.caption('これはstreamlitテスト用のアプリです。')

image = Image.open('./data/tempsnip.png')
st.image(image, width=200)