import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 읽기
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="안녕하세요. OpenAI 연결 테스트입니다."
)

print(response.output_text)