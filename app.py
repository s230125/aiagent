# 분류 모델 웹앱 만들기

import streamlit as st
import joblib as jl


# 1. 기계학습 모델 파일 로드

#model = jl.load('')


# 2. 모델 설명

st.title('환경에 따른 시험점수 예측')
st.subheader('내가 문제일까, 환경이 문제일까?')
col1,col2,col3 = st.columns(3)  

# 3. 데이터시각화

with col2:
    st.subheader('데이터 시각화1')
    st.image('시각화1.png')
    st.subheader('데이터 시각화2: 부모의 참여도')
    st.image('시각화2.png')
    st.subheader('데이터 시각화3: 부모의 교육 수준')
    st.image('시각화3.png')
    st.subheader('데이터 시각화4: 공부 시간')
    st.image('시각화4.png')

# 4. 모델 활용

with col1:
    st.subheader('사용자 정보 입력')
    b = st.selectbox('부모님이 교육에 얼마나 관여하나요?',['Low','Medium','High'])
    b = st.selectbox('공부를 위한 동기부여가 되어 있나요?',['Low','Medium','High'])
    b = st.selectbox('인터넷을 사용할 수 있나요?',['Yes','No'])
    b = st.selectbox('가족의 수입이 어느정도 되나요?',['Low','Medium','High'])
    b = st.selectbox('부모님이  얼마나 관여하나요?',['Private','Public'])
    b = st.selectbox('사교육을 받나요?',[''])
    b = st.selectbox('공부하는 데 있어서 친구의 영향이 어떤가요?',[''])
    b = st.selectbox('부모의 학력은 어떻게 되나요??',[''])


    
    
with col3:
    st.subheader('모델 설명')
    st.write('기계학습 알고리즘 - 선형 회귀')
    st.write('학습 데이터 출처(캐글)')
    st.write('훈련 데이터 : 4625개')
    st.write('테스트 데이터 : 1982개')

if st.button('점수 예측'):
    input_data = [[]]
    p = model.predict(input_data)
    st.write('인공지능이 예상한 당신의 점수는',p)
