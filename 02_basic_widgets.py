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

# 선택 상자
mbti = st.selectbox(
    "mbti를 선택해주세요.",
    ("ISFJ", "ENTJ", "몰라요")
)
if mbti == "ISFJ":
    st.write("올ㅋ")
elif mbti == "ENTJ":
    st.write("오잉")
else :
    st.write("모르시는구나")

# # 다중 선택 박스
# optinon = (
#     "좋아하는 과일?",
#     ["딸기", "바나나" "사과"],
#     ["딸기","바나나"]
# )
# st.multiselect(optinon)
# st.write(f"선택한 내용 : {optinon}")

# 슬라이더
values = st.slider(
    "범위 지정을 위해 사용",
    min_value=0.00,
    max_value=100.00
)
st.write(f"선택한 내용 : {values}")

# 텍스트 입력
title = st.text_input(
    "오늘 저녁 뭐먹을까"
)
st.write(f"{title} 맛있게 먹으렴")