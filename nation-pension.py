import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import streamlit as st

# 한글 폰트 설정
# plt.rcParams['font.family'] = "AppleGothic"
# Windows, 리눅스 사용자
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False

# 데이터 전처리, 각종 기능들을 모아놓은 클래스 

class PensionData():
    def __init__(self, filepath):
        self.df = pd.read_csv(os.path.join(filepath), encoding='cp949')
        self.pattern1 = '(\([^)]+\))'
        self.pattern2 = '(\[[^)]+\])'
        self.pattern3 = '[^A-Za-z0-9가-힣]'
        self.preprocess()
          
    def preprocess(self):
        self.df.columns = [
            '자료생성년월', '사업장명', '사업자등록번호', '가입상태', '우편번호',
            '사업장지번상세주소', '주소', '고객법정동주소코드', '고객행정동주소코드', 
            '시도코드', '시군구코드', '읍면동코드', 
            '사업장형태구분코드 1 법인 2 개인', '업종코드', '업종코드명', 
            '적용일자', '재등록일자', '탈퇴일자',
            '가입자수', '금액', '신규', '상실'
        ]
        df = self.df.drop(['자료생성년월', '우편번호', '사업장지번상세주소', '고객법정동주소코드', '고객행정동주소코드', '사업장형태구분코드 1 법인 2 개인', '적용일자', '재등록일자'], axis=1)
        df['사업장명'] = df['사업장명'].apply(self.preprocessing)
        df['탈퇴일자_연도'] =  pd.to_datetime(df['탈퇴일자']).dt.year
        df['탈퇴일자_월'] =  pd.to_datetime(df['탈퇴일자']).dt.month
        df['시도'] = df['주소'].str.split(' ').str[0]
        df = df.loc[df['가입상태'] == 1].drop(['가입상태', '탈퇴일자'], axis=1).reset_index(drop=True)
        df['인당금액'] = df['금액'] / df['가입자수']
        df['월급여추정'] =  df['인당금액'] / 9 * 100
        df['연간급여추정'] = df['월급여추정'] * 12
        self.df = df

        
    def preprocessing(self, x):
        x = re.sub(self.pattern1, '', x)
        x = re.sub(self.pattern2, '', x)
        x = re.sub(self.pattern3, ' ', x)
        x = re.sub(' +', ' ', x)
        return x
    
    def find_company(self, company_name):
        return self.df.loc[self.df['사업장명'].str.contains(company_name), ['사업장명', '월급여추정', '연간급여추정', '업종코드', '가입자수']]\
                  .sort_values('가입자수', ascending=False)
    
    def compare_company(self, company_name):
        company = self.find_company(company_name)
        code = company['업종코드'].iloc[0]
        df1 = self.df.loc[self.df['업종코드'] == code, ['월급여추정', '연간급여추정']].agg(['mean', 'count', 'min', 'max'])
        df1.columns = ['업종_월급여추정', '업종_연간급여추정']
        df1 = df1.T
        df1.columns = ['평균', '개수', '최소', '최대']
        df1.loc['업종_월급여추정', company_name] = company['월급여추정'].values[0]
        df1.loc['업종_연간급여추정', company_name] = company['연간급여추정'].values[0]
        return df1

    def company_info(self, company_name):
        company = self.find_company(company_name)
        return self.df.loc[company.iloc[0].name]
        
    def get_data(self):
        return self.df

@st.cache_data
def read_pensiondata():
    data = PensionData('https://www.dropbox.com/s/nxeo1tziv05ejz7/national-pension.csv?dl=1')
    return data


##### streamlit 기능 구현 ######

data = read_pensiondata()

# 1. 회사 이름 입력 받기
company_name = st.text_input(
    "회사 이름을 입력 해주세요.",
    placeholder="검색할 회사명 입력"
)

# 데이터도 존재하고, 회사의 이름도 잘 입력이 됐다면
if data and company_name:
    # 2. 회사의 이름을 이용해서 data에서 검색
    output = data.find_company(company_name=company_name)

    if len(output) > 0:
        # 3. 조회된 사업장의 정보 가져오기
        st.subheader(output.iloc[0]['사업장명'])
        #   사업장에 대한 구체적인 정보 조회
        info = data.company_info(company_name=company_name)
        st.markdown(
            f"""
                - `{info['주소']}`
                - 업종 코드명 `{info['업종코드명']}`
                - 총 근무자 : `{info['가입자수']}` 명
                - 신규 입사자 : `{info['신규']}` 명
                - 퇴사자 : `{info['상실']}` 명
            """
        )
        # 월 급여, 연봉, 가입자 수 출력
        col1, col2, col3 = st.columns(3)
        col1.text("월급여 추정")
        col1.markdown(f"`{int(output.iloc[0]['월급여추정'])}` 원")

        col2.text("연봉 추정")
        col2.markdown(f"`{int(output.iloc[0]['연간급여추정'])}` 원")

        col3.text("가입자 추정")
        col3.markdown(f"`{int(output.iloc[0]['가입자수'])}` 명")
    else:
        st.subheader("검색 결과가 없습니다.")