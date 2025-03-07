import streamlit as st

st.title("Hello World")

# 각 아티클의 제목
st.header("여기는 헤더")
st.subheader("이것은 소제목")

# 캡션 - 데이터 프레임이나 이미지를 설명하기 위한 곳
st.caption("여기는 캡션입니다.")

# 코드 표현
my_sample_code = """
def function_name():
    print("Hello Wolrd")
"""

st.code(my_sample_code, language="python")

# 일반 텍스트
st.text("이곳은 텍스트의 자리여")

# 마크다운 입력
st.markdown("이것은 **마크다운**으로 입력된 텍스트다.")
st.markdown("색상을 :green[초록색]으로, :blue[파란색]이면서 굵게 표현!")

# Latex 문법을 Markdown으로 작성
# - 인라인 : $수식$
st.markdown("$a^2+b^2=c^2$ 이것은 피타고라스 정리")
# 블록 수식은 latex
st.latex("a^2+b^2=c^2")