import streamlit as st
import FinanceDataReader as fdr
import datetime
with st.sidebar :
    date = st.date_input(
        "조회 시작일 선택",
        datetime.datetime(2025, 1, 1)
    )

    code = st.text_input(
        label='종목코드',
        value='',
        placeholder='종목 코드를 입력하세요.'
    )

    # 날짜와 코드가 잘 들어있어야 주가 조회
if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close'] # CLose : 종가
    tab1, tab2 = st.tabs(['차트', '데이터'])
    
    with tab1:
        st.line_chart(data)
    with tab2:
        st.dataframe(data)

# with st.expander:
#     st.markdown('''
#         - Open: 시가
#         - High: 고가
#         - Low: 저가
#         - Close: 종가
#         - Adj Close: 수정 종가
#         - Volumn: 거래량
#         ''')