import streamlit as st
import pandas as pd

df = pd .DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 데이터 프레임 표현
st.dataframe(df, use_container_width=True)

# 데이터 프레임을 테이블로 표현
# 데이터 프레임과 다른 점은 인터렉티브한 UI를 제공하지 않는다.
st.table(df)

# 메트릭
st.metric(label="삼성전자", value="55,000원", delta="-1,200원")
st.metric(label="테슬라", value="263$", delta="3$")

# 컬럼으로 영역을 나눠서 표현
col1, col2, col3 = st.columns(3)

col1.metric(label="삼성전자", value="55,000원", delta="-1,200원")
col2.metric(label="테슬라", value="263$", delta="3$")
col3.metric(label='엔비디아', value="110%", delta='-2$')