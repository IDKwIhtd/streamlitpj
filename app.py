import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .main {
        text-align: center; 
    }
    </style>
""", unsafe_allow_html=True)

# 스타일 적용
st.markdown("""
    <style>
    .title {
        font-style: italic;
        text-align: center; 
        font-size: 2.5em;  
        font-weight: bold; 
    }
    .icon {
        font-style: normal;}
    </style>
""", unsafe_allow_html=True)

# HTML 기반 제목 출력
st.markdown("""
    <div class="title">
        <span class="icon">🎁</span>
        <span style="color:grey;">MERRY</span> 
        <span style="color:red;">X</span>
        <span style="color:green;">-</span>
        <span style="color:red;">M</span>
        <span style="color:green;">A</span>
        <span style="color:red;">S</span>    
        <span class="icon">🎁</span>    
            </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .ascii-art {
        font-family: monospace;
        white-space: pre-wrap; 
        text-align: center; 
        line-height: 1.5; 
    }
    </style>
""", unsafe_allow_html=True)

# '.'을 '&nbsp;'로
def convert_dots_to_nbsp(ascii_art_line):
    """
    '.'을 '&nbsp;'로 변환
    :param ascii_art_line: 아스키 아트 문자열 한 줄
    :return: 변환된 문자열
    """
    return ascii_art_line.replace('.', '&nbsp;')

# ASCII 아트 데이터
ascii_art_lines = [
    "....✦.........................✧.............✦........................✦..",
    "...................✦..............🌟......................✧............",
    "....✧............................*✨*..........✧........................",
    ".........✦...........✧.........✨▲▲▲✨................✦...........✦...",
    "..✦...........................*✨*****✨*...............................",
    "................✧............✨*********✨................✧.............",
    ".....✧......................*✨***********✨*...........................✧",
    ".................................|||||.................................",
    "..................................|||||.................................."
]

# AA Streamlit에 출력
for line in ascii_art_lines:
    converted_line = convert_dots_to_nbsp(line)  # '.'을 '&nbsp;'로 변환
    st.markdown(f"<p class='ascii-art'>{converted_line}</p>", unsafe_allow_html=True)




st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

age = st.slider("몇 살이예요?", 0, 100, 25)
st.write("나는 ", age, "살!")

st.write(" ")
st.write(" ")
st.write(" ")

option = st.selectbox(
    "선물을 어디에 두면 좋을지 알려주세요",
    ("문앞에 두세요", "양말 속에 넣어주세요", "굴뚝으로 떨어뜨려주세요", "직접 받을게요"))

st.write("선물은 ", option)

st.write(" ")
st.write(" ")
st.write(" ")



with st.form("form_v2"):
    text1 = st.text_input("이름", key="text1_with_form_v2")
    text2 = st.text_area("받고 싶은 선물", key="text2_with_form_v2")
    text3 = st.text_area("주소", key="text3_with_form_v2")
    submitted = st.form_submit_button("주세요")

if submitted:
    st.markdown("**이름**")  
    st.write(text1)  
    st.markdown("**받고 싶은 선물**")
    st.write(text2)  
    st.markdown("**주소**")
    st.write(text3)  
else:
    st.write("")



st.write("")
st.write("")
st.write("")

st.write("입력정보를 확인하고 checkbox를 클릭해주세요!")
agree = st.checkbox("확인완료")

if agree:
    st.write("출발해요🎅🏼")