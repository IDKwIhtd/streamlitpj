from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY1")

# OpenAI Client 초기화
client = OpenAI(api_key=api_key)

# Chat Completion 생성
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "귀찮ㅋㅋ"
        },
        {
            "role": "system",
            "content": "최대한 한국어 원문의 느낌을 일본어의 느낌으로 살려서 일본인이 쓴 것처럼 일본어로 출력해줘."
        }
    ],
    # 하이퍼파라미터
    temperature=1, # 응답을 랜덤하게 생성 - 기본값
    max_tokens=2048, # 응답 최대 길이 (토큰단위) - 기본값 : max_token = 4096
    top_p=1, # Nucleus Sampling 비활성화 (모든 확률 고려)
    frequency_penalty=0, # 같은 단어를 반복하는 패널티 없음
    presence_penalty=0 # 새로운 주제를 추가하는 패널티 없음
)

# 응답 출력
print(response.choices[0].message.content)

#role
# system : AI가 어떤 스타일로 답변해야 하는지 사전에 정해주는 설정
# user : 실제 사용자가 AI에게 입력하는 질문
# assistant : AI가 생성하는 응답, 이전 대화 내용(시스템 메세지 포함)을 참고해서 대답을 생성