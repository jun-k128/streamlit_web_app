import streamlit as st
import pandas as pd

df = pd.read_excel('./data/data.xlsx', index_col='月')
#df = df.set_index('Date')
st.dataframe(df)
#st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])