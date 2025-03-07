import streamlit as st
from datetime import datetime as dt
import datetime

button = st.button("버튼을 눌러보세요!")

# button을 눌렀을 때 메시지 출력
if button :
    st.write(":blue[버튼] 컴온")

# checkbox
agree = st.checkbox("동의?")
if agree :
    st.write("보감")

# 라디오 버튼 - 여러 선택지 중 하나 선택
mbti = st.radio(
    "mbti를 선택해주세요.",
    ("ISFJ", "ENTJ", "몰라요")
)
if mbti == "ISFJ":
    st.write("올ㅋ")
elif mbti == "ENTJ":
    st.write("오잉")
else :
    st.write("모르시는구나")