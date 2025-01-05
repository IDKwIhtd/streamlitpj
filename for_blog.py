import streamlit as st

st.title("✏️필기내용을 정리하고 보충해요📝")

title = st.text_input("필기내용을 넣어주세요")
st.write("뭐라는지 전혀 모르겠음", title)


if st.button('입력하기'):
    url = ''+title
    st.write(title)
    st.image(url)