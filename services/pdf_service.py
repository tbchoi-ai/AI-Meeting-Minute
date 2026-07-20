import os

from datetime import datetime


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)


from reportlab.lib.enums import (
    TA_CENTER,
    TA_RIGHT
)


from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont



# ==================================================
# 출력 폴더
# ==================================================

OUTPUT_FOLDER = "outputs"



# ==================================================
# 한글 폰트 자동 탐색
# ==================================================

FONT_CANDIDATES = [

    r"C:\Windows\Fonts\NotoSansKR-Regular.ttf",

    r"C:\Windows\Fonts\malgun.ttf",

    r"C:\Windows\Fonts\NanumGothic.ttf"

]


FONT_PATH = None


for font in FONT_CANDIDATES:

    if os.path.exists(font):

        FONT_PATH = font
        break



if FONT_PATH is None:

    raise FileNotFoundError(
        "한글 폰트를 찾을 수 없습니다."
    )



pdfmetrics.registerFont(

    TTFont(
        "KoreanFont",
        FONT_PATH
    )

)



# ==================================================
# PDF 생성
# ==================================================

def create_pdf(
        korean_text,
        english_text
):


    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )


    filename = os.path.join(
        OUTPUT_FOLDER,
        "meeting_minutes.pdf"
    )



    document = SimpleDocTemplate(

        filename,

        rightMargin=50,

        leftMargin=50,

        topMargin=50,

        bottomMargin=50

    )



    styles = getSampleStyleSheet()



    # ==================================================
    # Style 개선
    # ==================================================

    title_style = ParagraphStyle(

        "TitleStyle",

        parent=styles["Heading1"],

        fontName="KoreanFont",

        fontSize=16,

        leading=20,

        alignment=TA_CENTER,

        spaceAfter=8

    )



    heading_style = ParagraphStyle(

        "HeadingStyle",

        parent=styles["Heading2"],

        fontName="KoreanFont",

        fontSize=13,

        leading=16,

        spaceBefore=5,

        spaceAfter=5

    )



    sub_heading_style = ParagraphStyle(

        "SubHeadingStyle",

        parent=styles["Heading3"],

        fontName="KoreanFont",

        fontSize=11,

        leading=14,

        spaceBefore=4,

        spaceAfter=2

    )



    body_style = ParagraphStyle(

        "BodyStyle",

        parent=styles["BodyText"],

        fontName="KoreanFont",

        fontSize=10,

        leading=13,

        spaceBefore=0,

        spaceAfter=2

    )



    date_style = ParagraphStyle(

        "DateStyle",

        parent=styles["Normal"],

        fontName="KoreanFont",

        fontSize=9,

        leading=12,

        alignment=TA_RIGHT

    )



    story = []



    # ==================================================
    # Title
    # ==================================================

    story.append(

        Paragraph(

            "AI Meeting Minutes",

            title_style

        )

    )


    story.append(

        Spacer(
            1,
            8
        )

    )



    # ==================================================
    # Date
    # ==================================================

    story.append(

        Paragraph(

            f"Created : {datetime.now().strftime('%Y-%m-%d %H:%M')}",

            date_style

        )

    )



    story.append(

        Spacer(
            1,
            8
        )

    )



    # ==================================================
    # Korean
    # ==================================================

    story.append(

        Paragraph(

            "■ 한국어 회의록",

            heading_style

        )

    )



    if isinstance(korean_text, dict):

        add_korean_pdf(

            story,

            korean_text,

            sub_heading_style,

            body_style

        )


    else:


        for line in korean_text.split("\n"):


            if line.strip():

                story.append(

                    Paragraph(

                        line,

                        body_style

                    )

                )



    story.append(

        Spacer(
            1,
            10
        )

    )



    # ==================================================
    # English
    # ==================================================

    story.append(

        Paragraph(

            "■ English Meeting Minutes",

            heading_style

        )

    )



    for line in english_text.split("\n"):


        if line.strip():

            story.append(

                Paragraph(

                    line,

                    body_style

                )

            )



    document.build(story)



    return filename





# ==================================================
# 한국어 회의록 생성
# ==================================================

def add_korean_pdf(

        story,

        minutes,

        sub_heading_style,

        body_style

):


    sections = [

        (
            "회의 제목",
            minutes.get(
                "meeting_title",
                ""
            )
        ),

        (
            "회의 목적",
            minutes.get(
                "meeting_purpose",
                ""
            )
        ),

        (
            "참석자",
            minutes.get(
                "participants",
                ""
            )
        )

    ]



    for title, text in sections:


        story.append(

            Paragraph(

                title,

                sub_heading_style

            )

        )


        story.append(

            Paragraph(

                text,

                body_style

            )

        )


        story.append(

            Spacer(
                1,
                3
            )

        )



    # ==================================================
    # Discussion
    # ==================================================

    story.append(

        Paragraph(

            "논의 사항",

            sub_heading_style

        )

    )


    for item in minutes.get(
        "discussion",
        []
    ):


        story.append(

            Paragraph(

                "• " + item,

                body_style

            )

        )



    # ==================================================
    # Decisions
    # ==================================================

    story.append(

        Paragraph(

            "결정 사항",

            sub_heading_style

        )

    )


    for item in minutes.get(
        "decisions",
        []
    ):


        story.append(

            Paragraph(

                "• " + item,

                body_style

            )

        )



    # ==================================================
    # Action Items
    # ==================================================

    story.append(

        Paragraph(

            "Action Items",

            sub_heading_style

        )

    )


    actions = minutes.get(

        "action_items",

        []

    )



    if actions:


        data = [

            [
                "담당자",
                "업무",
                "완료일"
            ]

        ]



        for action in actions:


            data.append(

                [

                    action.get("owner",""),

                    action.get("task",""),

                    action.get("due_date","")

                ]

            )



        table = Table(

            data,

            colWidths=[80,250,80]

        )



        table.setStyle(

            TableStyle(

                [

                    (
                        "GRID",
                        (0,0),
                        (-1,-1),
                        0.5,
                        None
                    )

                ]

            )

        )


        story.append(table)



    # ==================================================
    # Next Schedule
    # ==================================================

    story.append(

        Paragraph(

            "다음 일정",

            sub_heading_style

        )

    )


    story.append(

        Paragraph(

            minutes.get(
                "next_schedule",
                ""
            ),

            body_style

        )

    )