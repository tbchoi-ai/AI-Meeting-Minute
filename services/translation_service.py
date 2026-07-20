from openai import OpenAI
from dotenv import load_dotenv
import os
import json


# .env 로드
load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



def translate_meeting(meeting_minutes):


    # Dictionary 형태이면 JSON 문자열 변환

    if isinstance(meeting_minutes, dict):

        meeting_minutes = json.dumps(
            meeting_minutes,
            ensure_ascii=False,
            indent=4
        )


    prompt = f"""
당신은 전문 기술 번역가입니다.

다음 한국어 회의록을
자연스러운 비즈니스 영어 회의록으로 번역하세요.

조건:

1. 회의록 구조를 유지할 것
2. 기술 용어는 정확히 번역할 것
3. 군사/IT/SW 분야 용어는 전문 용어 사용
4. JSON 구조라면 JSON 구조 유지


한국어 회의록:

{meeting_minutes}

"""


    response = client.responses.create(

        model="gpt-5-nano",

        input=prompt

    )


    return response.output_text