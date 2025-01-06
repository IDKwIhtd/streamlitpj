from openai import OpenAI
import os

# OpenAI Client 초기화
client = OpenAI(
    api_key="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" # 여기에 API 키를 직접 입력
)

# Chat Completion 생성
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "귀찮"
        }
    ],
    response_format={
        "type": "text"
    },
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 응답 출력
print(response.choices[0].message.content)