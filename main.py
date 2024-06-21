#pip install streamlit
import streamlit as st
from PIL import Image
import exchange_rate 

#터미널에 streamlit run 파일명

#로그인화면 만들기 사이드바
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value='hi', max_chars=15)
user_pw = st.sidebar.text_input("비밀번호 입력", value='1234', type="password", max_chars=15)

if user_pw == "1234" and user_id =="hi":

    #이미지 목록을 콤보상자 셀렉트박스로 만들기
    st.sidebar.header("나의 포트폴리오")
    # sel_options = ['','진주 귀걸이를 한 소녀','별이 빛나는 밤','절규','생명의 나무','월하정인']
    # user_opt = st.sidebar.selectbox("좋아하는 작품은?",sel_options,index=0)
    # st.sidebar.write('*선택한 그림은',user_opt)
    menu = st.sidebar.radio('메뉴 선택',['환율 조회','부동산 조회(EDA)','인공지능으로 예측/분류'],index=None)

    if menu == '환율 조회':
        exchange_rate.exchange_main() #함수 불러왔다
        st.sidebar.write('환율 조회')
    elif menu == '부동산 조회(EDA)':
        st.sidebar.write('부동산 조회(EDA)')
    elif menu == '인공지능으로 예측/분류':
        st.sidebar.write('인공지능으로 예측/분류')
    else:
        st.sidebar.write('메뉴 선택해주세요')



    # #메인화면
    # st.subheader('결과', divider='rainbow')
