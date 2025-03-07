import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 시각화를 캔버스 안에다 수행
# 캔버스 안에 있는 그래프 -> figure
# figure를 streamlit으로 표현

# DataFrame 생성
data = pd.DataFrame({
    'name': ['a', 'b', 'c'],
    'age': [22, 31, 25],
    'weight': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

# 노트북에서는 신경 안썼는데... 시각화 할 때 plt.figure() 이용해 새로운 canvas를 만들어낸다
fig, ax = plt.subplots()
ax.bar(data['name'], data['age'])
st.pyplot(fig)

bar_seaborn = sns.barplot(data=data,
                            x='name',
                            y='age',
                            ax=ax,
                            palette='Set2')
figure = bar_seaborn.get_figure()
st.pyplot(fig)
