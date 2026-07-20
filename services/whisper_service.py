from openai import OpenAI
from dotenv import load_dotenv
import os


# ==================================================
# .env 읽기
# ==================================================

load_dotenv()



# ==================================================
# OpenAI Client
# ==================================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



# ==================================================
# Whisper Speech To Text
# ==================================================

def speech_to_text(audio_path):

    try:


        with open(
            audio_path,
            "rb"
        ) as audio_file:


            transcript = client.audio.transcriptions.create(

                model="gpt-4o-mini-transcribe",

                file=audio_file,

                language="ko"

            )



        text = transcript.text



        # ==========================================
        # Transcript 가독성 개선
        # ==========================================

        text = text.replace(
            ". ",
            ".\n"
        )


        text = text.replace(
            "다.",
            "다.\n"
        )


        text = text.replace(
            "요.",
            "요.\n"
        )


        return text



    except Exception as e:


        print(
            "Whisper 오류:",
            e
        )


        return ""