from openai import OpenAI
from dotenv import load_dotenv

import os
import json


# ==================================================
# 환경 변수
# ==================================================

load_dotenv()



# ==================================================
# OpenAI Client
# ==================================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



# ==================================================
# Meeting Summary
# ==================================================

def summarize_meeting(transcript):


    prompt = f"""

당신은 전문 회의록 작성 전문가입니다.

아래 회의 내용을 분석하여
반드시 JSON 형식으로만 작성하세요.


출력 형식:

{{
 "meeting_title":"",
 "meeting_purpose":"",
 "participants":"",

 "discussion":[
    ""
 ],

 "decisions":[
    ""
 ],

 "action_items":[

    {{
     "owner":"",
     "task":"",
     "due_date":""
    }}

 ],

 "next_schedule":""

}}



회의 내용:

{transcript}

"""



    response = client.responses.create(

        model="gpt-5-nano",

        input=prompt

    )



    result = response.output_text



    # ==============================================
    # JSON 변환
    # ==============================================

    try:

        meeting_minutes = json.loads(result)


    except json.JSONDecodeError:


        print(
            "JSON 변환 실패"
        )


        print(result)


        meeting_minutes = {

            "meeting_title":"",

            "meeting_purpose":"",

            "participants":"",

            "discussion":[
                result
            ],

            "decisions":[],

            "action_items":[],

            "next_schedule":""

        }



    return meeting_minutes