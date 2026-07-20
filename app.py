from flask import Flask, render_template, request, send_file
import os

from services.whisper_service import speech_to_text
from services.summary_service import summarize_meeting
from services.translation_service import translate_meeting
from services.word_service import create_word
from services.pdf_service import create_pdf

app = Flask(__name__)

# 업로드 다운로드 폴더 지정
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    print("업로드 시작")

    # 파일이 없는 경우
    if "audioFile" not in request.files:
        return "파일이 없습니다."

    file = request.files["audioFile"]

    # 파일명이 없는 경우
    if file.filename == "":
        return "파일명이 없습니다."

    print(file.filename)

    # 저장 위치
    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    # 파일 저장
    file.save(save_path)
    print("파일 저장 완료")

    # Whisper 실행
    transcript = speech_to_text(save_path)
    print("Whisper 완료")

    # GPT 회의록 생성
    meeting_minutes = summarize_meeting(transcript)

    print("GPT 완료")
    print("==============================")
    print("meeting_minutes type:")
    print(type(meeting_minutes))

    print("meeting_minutes 내용:")
    print(meeting_minutes)

    print("==============================")

    # 영문 번역
    english_minutes = translate_meeting(meeting_minutes)
    print("번역 완료")

    # Word 생성
    word_file = create_word(
        meeting_minutes,
        english_minutes
    )

    print("Word 생성 완료")

    # PDF 생성
    pdf_file = create_pdf(
        meeting_minutes,
        english_minutes
    )

    print("PDF 생성 완료")

    return render_template(
        "index.html",
        transcript=transcript,
        result=meeting_minutes,
        english=english_minutes,
        word_file=word_file,
        pdf_file=pdf_file
    )

@app.route("/download/word")
def download_word():

    return send_file(
        os.path.join(
            OUTPUT_FOLDER,
            "meeting_minutes.docx"
        ),
        as_attachment=True
    )

@app.route("/download/pdf")
def download_pdf():

    return send_file(
        os.path.join(
            OUTPUT_FOLDER,
            "meeting_minutes.pdf"
        ),
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)