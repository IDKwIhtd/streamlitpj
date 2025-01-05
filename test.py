


st.subheader("_WE_ are :blue[cool] :sunglasses:")


st.write("Hello, *World!* :sunglasses:")
st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        
        }
    )
)



st.text("""



ㅤ ㅤ ㅤ ㅤ 🌟
ㅤ ㅤ ㅤ ㅤ*✨*
ㅤ ㅤ ㅤ ✨***✨
ㅤ ㅤ  *✨*****✨*
ㅤ ㅤ ✨*********✨
ㅤ  *✨***********✨*
ㅤ ㅤ ㅤ ㅤ|||||
ㅤ ㅤ ㅤ ㅤ|||||
ㅤ ㅤ
"""
)


col1, col2 = st.columns(2)  # 두 개의 컬럼 생성

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우", key="text1_no_form")
    text2 = st.text_input("form을 이용하지 않는 경우", key="text2_no_form")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)

with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("form을 이용하는 경우", key="text3_with_form")
        text4 = st.text_input("form을 이용하는 경우", key="text4_with_form")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3)
            st.write("2번 입력값: " + text4)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")


col1, col2 = st.columns(2) # 두 개의 컬럼 생성 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우")
    text2 = st.text_area("form을 이용하지 않는 경우")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)
    


col1, col2 = st.columns(2)  # 두 개의 컬럼 생성

with col1:
    text1_no_form = st.text_input("form을 이용하지 않는 경우", key="text1_no_form_v2")
    text2_no_form = st.text_area("form을 이용하지 않는 경우", key="text2_no_form_v2")
    st.write("1번 입력값: " + text1_no_form)
    st.write("2번 입력값: " + text2_no_form)

with col2:
    with st.form("form을 사용합니다_v2"):
        text3_with_form = st.text_input("form을 이용하는 경우", key="text3_with_form_v2")
        text4_with_form = st.text_area("form을 이용하는 경우", key="text4_with_form_v2")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3_with_form)
            st.write("2번 입력값: " + text4_with_form)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")



