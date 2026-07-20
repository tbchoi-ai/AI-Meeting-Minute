# AI Meeting Minute System

AI 기반 자동 회의록 생성 시스템

(OpenAI Whisper + GPT + Flask + Document Generator)

---

## 1. Project Overview

AI Meeting Minute System은 회의 음성 데이터를 입력받아

1. 음성 인식 (Speech-to-Text)
2. AI 기반 회의 내용 분석 및 요약
3. 한국어 회의록 생성
4. 영어 회의록 자동 번역
5. Word / PDF 보고서 생성

까지 자동 수행하는 AI 기반 회의록 자동화 시스템입니다.

본 시스템은 생성형 AI 기술을 활용하여 회의 기록 업무를 자동화하고,
회의 결과 공유 및 업무 추적 효율성을 향상시키는 것을 목표로 합니다.

---

# 2. System Architecture
            Audio File
                |
                v
      +----------------+
      | Flask Web App  |
      +----------------+
                |
                v
      +----------------+
      | Whisper STT    |
      | Speech To Text |
      +----------------+
                |
                v
      +----------------+
      | GPT Meeting    |
      | Summary Engine |
      +----------------+
                |
      +---------+---------+
      |                   |
      v                   v
      Korean Minutes English Translation
| |
+---------+---------+
|
v
+----------------+
| Document |
| Generator |
| Word / PDF |
+----------------+

---

# 3. Main Features

## 3.1 Speech Recognition

OpenAI Whisper 기반 음성 인식 기능

지원 기능:

- 한국어 음성 변환
- 회의 음성 Text 변환
- Transcript 생성


Technology:
OpenAI Whisper
gpt-4o-mini-transcribe
---

## 3.2 AI Meeting Summary

GPT 기반 회의 분석 기능

자동 생성 항목:

- 회의 제목
- 회의 목적
- 참석자
- 주요 논의 사항
- 결정 사항
- Action Items
- 다음 일정


Output Example:

```json
{
 "meeting_title":
 "AI 시스템 개발 방향 회의",

 "discussion":
 [
  "음성 인식 모듈 개선 방안 검토"
 ],

 "decisions":
 [
  "GPT 기반 요약 기능 적용"
 ]
}

3.3 Automatic Translation

한국어 회의록을 영어 회의록으로 자동 변환합니다.

Features:

Business English Translation
Meeting Format 유지
Technical terminology 적용
3.4 Document Generation

회의 결과를 자동으로 문서화합니다.

지원:

Microsoft Word (.docx)
PDF (.pdf)

Generated Files:

outputs/

 ├── meeting_minutes.docx

 └── meeting_minutes.pdf
4. Technology Stack
Backend
Technology	Description
Python	Programming Language
Flask	Web Framework
OpenAI API	Generative AI Service
AI Model
Model	Purpose
gpt-4o-mini-transcribe	Speech Recognition
gpt-5-nano	Meeting Summary & Translation
Document
Library	Purpose
python-docx	Word Generation
ReportLab	PDF Generation
5. Project Structure
AI-Meeting-Minute

│
├── app.py
│
├── services
│   │
│   ├── whisper_service.py
│   ├── summary_service.py
│   ├── translation_service.py
│   ├── word_service.py
│   └── pdf_service.py
│
├── templates
│   └── index.html
│
├── static
│   └── css
│       └── style.css
│
├── uploads
│
├── outputs
│
├── .env
│
├── requirements.txt
│
└── README.md

6. Installation
6.1 Clone Repository
git clone https://github.com/tbchoi-ai/AI-Meeting-Minute.git

cd AI-Meeting-Minute
6.2 Create Virtual Environment

Windows:

python -m venv venv

Activate:

venv\Scripts\activate
6.3 Install Packages
pip install -r requirements.txt
7. Environment Configuration

Create .env file.

Example:

OPENAI_API_KEY=your_api_key

주의:

API Key는 GitHub에 업로드하지 않습니다.

8. Execute

Run Flask Server:

python app.py

Browser:

http://127.0.0.1:5000
9. Usage
Step 1

Upload meeting audio file

Supported:

wav
mp3
m4a
Step 2

AI Processing

Process:

Audio
 ↓
Whisper
 ↓
Transcript
 ↓
GPT Summary
 ↓
Translation
 ↓
Document
Step 3

Download Result

Generated:

Word Meeting Minutes

PDF Meeting Minutes
10. Future Development
Phase 2
Speaker Diarization

화자 자동 구분 기능

Example:

[Speaker 1]
개발 일정 설명

[Speaker 2]
시험 계획 제안
Phase 3
RAG Based Meeting Search

Architecture:

Meeting Data

    ↓

Embedding

    ↓

Vector Database

    ↓

Semantic Search


Example:

"지난 회의에서 결정한 개발 일정은?"
Phase 4
Enterprise AI Meeting Assistant

Future capability:

Multi-user support
Meeting history management
Knowledge database integration
Enterprise authentication
11. License

This project is for educational and research purposes.

12. Author

Taebong Choi

AI / Software Engineering Research


---

## README 저장 후 GitHub 반영 절차

PowerShell에서:

```powershell
git add README.md


