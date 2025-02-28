from openai import OpenAI
import os
import streamlit as st

api_key = os.getenv("OPENAI_API_KEY0")

# OpenAI Client 초기화
client = OpenAI(api_key=api_key)

st.title("🇰🇷리얼 일본어 번역 봇🇯🇵")

prompt = st.text_input("입력")

if st.button("전송"):
    with st.spinner("번역중..."):

        # Chat Completion 생성
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt},
                {
                    "role": "system",
                    "content": "최대한 일본사람인거야!! 한국어가 어떤 느낌으로 쓰였는지 몇살의 어떤 사람이 왜 쓴건지 어떤 이미지를 주고싶은지 의도까지 파악해서 일본인에게 투영해 !! 최대한 한국어의 느낌을 일본어의 느낌으로 살려서 일본인이 쓴 것처럼 일본어로 출력해줘. 마치 현지어 번역기처럼. 번역된 일본어만 출력해줘.",
                },
            ],
            # 하이퍼파라미터
            temperature=1,  # 응답을 랜덤하게 생성 - 기본값
            max_tokens=2048,  # 응답 최대 길이 (토큰단위) - 기본값 : max_token = 4096
            top_p=1,  # Nucleus Sampling 비활성화 (모든 확률 고려)
            frequency_penalty=0,  # 같은 단어를 반복하는 패널티 없음
            presence_penalty=0,  # 새로운 주제를 추가하는 패널티 없음
        )
    st.write(response.choices[0].message.content)
