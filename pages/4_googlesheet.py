import streamlit as st
import pandas as pd

st.title("Google Sheet 연동")

gsid = st.secrets["gsid"]

url = f"https://docs.google.com/spreadsheets/d/{gsid}/export?format=csv&gid=0"
# url의 뒤쪽을 EXPORT의 형태로 바꿔야하지만 연동이 됨!

data = pd.read_csv(url)
# st.dataframe(data) # 표로 나타내기

# 문항 1,2,3 만들기

question1 = data.iloc[0,1] # 행렬의 entity 번호라고 생각하면 됨
question2 = data.iloc[1,1]
question3 = data.iloc[2,1]

st.write(question1)
a1 = st.text_input("문항 1답변 : ")

st.write(question2)
a2 = st.text_input("문항 2답변 : ")

st.write(question3)
a3 = st.text_input("문항 3답변 : ")