# 분류 모델 웹앱 만들기

import streamlit as st
import joblib as jl


# 1. 기계학습 모델 파일 로드

model = jl.load('linear_regression_model.pkl')


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
    a = st.number_input('1주일 동안 공부하는 시간을 입력해주세요.',value=0)
    b = st.number_input('지난 시험의 점수를 입력해주세요.',value=0)
    c = st.selectbox('부모님이 교육에 얼마나 관여하나요? (낮음 : 0 , 중간 : 1, 높음 : 2)',[0,1,2])
    d = st.selectbox('공부를 위한 동기부여가 되어 있나요? (낮음 : 0 , 중간 : 1, 높음 : 2)',[0,1,2])
    e = st.selectbox('인터넷을 사용할 수 있나요? (아니오 : 0, 네 : 1)',[0,1])
    f = st.selectbox('가족의 수입이 어느정도 되나요? (낮음 : 0 , 중간 : 1, 높음 : 2)',[0,1,2])
    g = st.selectbox('선생님의 교육 수준은 어떤가요? (낮음 : 0 , 중간 : 1, 높음 : 2)',[0,1,2])
    h = st.selectbox('공부하는 데 있어서 친구의 영향이 어떤가요? (부정적 : 0, 영향 없음 : 1, 긍정적 : 2)',[0,1,2])
    i = st.selectbox('부모의 학력은 어떻게 되나요? (고등학교 : 0, 대학교 : 1, 대학원 : 2)',[0,1,2])


    
    
with col3:
    st.subheader('모델 설명')
    st.write('기계학습 알고리즘 - 선형 회귀')
    st.write('학습 데이터 출처(캐글)')
    st.write('훈련 데이터 : 4625개')
    st.write('테스트 데이터 : 1982개') 
    st.write('**이 모델의 정확도는 0.3으로 예측 결과를 진지하게 받아들이기 보단 재미로 보는 편이 좋을 것 같습니다.**')

if st.button('점수 예측'):
    input_data = [[a,b,c,d,e,f,g,h,i]]
    p = model.predict(input_data)
    st.write('인공지능이 예상한 당신의 점수는',p)
