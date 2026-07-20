from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 업로드 폴더 지정
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# 폴더가 없으면 자동 생성
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    # 파일이 없는 경우
    if "audioFile" not in request.files:
        return "파일이 없습니다."

    file = request.files["audioFile"]

    # 파일명을 유지하여 저장
    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(save_path)

    return f"업로드 성공 : {file.filename}"


if __name__ == "__main__":
    app.run(debug=True)