import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

response = client.images.generate(
    model = "dall-e-3",
    prompt = "반짝이는 숲속의 요정들",
    size = "1024x1024",
    n = 1,
)

image_url = response.data[0].url
print(image_url)