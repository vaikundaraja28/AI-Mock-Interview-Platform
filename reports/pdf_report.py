from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)


def generate_report(
    filename,
    user,
    role,
    difficulty,
    company,
    question,
    answer,
    evaluation,
    overall_score,
    followup_question="Not Available",
    followup_answer="Not Available",
    followup_evaluation="Not Available",
    career_advice="Not Available",
    interview_questions=None,
    interview_answers=None,
    interview_evaluations=None,
    scores=None
):

    styles = getSampleStyleSheet()

    if interview_questions is None:
        interview_questions = []

    if interview_answers is None:
        interview_answers = []

    if interview_evaluations is None:
        interview_evaluations = []

    if scores is None:
        scores = []

    # -------------------------
    # Title Style
    # -------------------------

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0F62FE"),
        fontSize=22,
        spaceAfter=15
    )

    # -------------------------
    # Heading Style
    # -------------------------

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#0F62FE"),
        fontSize=14,
        spaceBefore=10,
        spaceAfter=8
    )

    # -------------------------
    # Body Style
    # -------------------------

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14
    )

    # -------------------------
    # Career Coach Style
    # -------------------------

    career_style = ParagraphStyle(
        "CareerStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        spaceAfter=5
    )

    # -------------------------
    # PDF Document
    # -------------------------

    pdf = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    story = []

    # -------------------------
    # Header
    # -------------------------

    header = Table(
        [
            [
                Paragraph(
                    "AI MOCK INTERVIEW PLATFORM",
                    title_style
                )
            ]
        ],
        colWidths=[
            6.5 * inch
        ]
    )

    header.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#E8F1FF")
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.HexColor("#0F62FE")
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )
            ]
        )
    )

    story.append(
        header
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    # -------------------------
    # Report Title
    # -------------------------

    story.append(
        Paragraph(
            "AI Mock Interview Report",
            title_style
        )
    )

    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor("#0F62FE")
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )

    # -------------------------
    # Candidate Details
    # -------------------------

    story.append(
        Paragraph(
            "Candidate Details",
            heading_style
        )
    )

    candidate_data = [
        [
            "Name",
            user
        ],
        [
            "Role",
            role
        ],
        [
            "Company",
            company
        ],
        [
            "Difficulty",
            difficulty
        ],
        [
            "Date",
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )
        ]
    ]

    candidate_table = Table(
        candidate_data,
        colWidths=[
            1.5 * inch,
            4.5 * inch
        ]
    )

    candidate_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#DCEBFF")
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                )
            ]
        )
    )

    story.append(
        candidate_table
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    # -------------------------
    # Interview Summary
    # -------------------------

    story.append(
        Paragraph(
            "Interview Summary",
            heading_style
        )
    )

    summary_data = [
        [
            "Overall Score",
            f"{overall_score}/10"
        ],
        [
            "Interview Status",
            "Completed"
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[
            180,
            180
        ]
    )

    summary_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#E8F0FE")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, -1),
                    colors.black
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )
            ]
        )
    )

    story.append(
        summary_table
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    # -------------------------
    # Interview Question
    # -------------------------

    story.append(
        Paragraph(
            "Interview Question",
            heading_style
        )
    )

    story.append(
        Paragraph(
            question.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )

    # -------------------------
    # Candidate Answer
    # -------------------------

    story.append(
        Paragraph(
            "Candidate Answer",
            heading_style
        )
    )

    story.append(
        Paragraph(
            answer.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )

    # -------------------------
    # AI Evaluation
    # -------------------------

    story.append(
        Paragraph(
            "AI Evaluation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            evaluation.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    # -------------------------
    # Complete Interview Questions
    # -------------------------

    if interview_questions:

        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=colors.HexColor("#0F62FE")
            )
        )

        story.append(
            Spacer(
                1,
                15
            )
        )

        story.append(
            Paragraph(
                "Complete Interview Assessment",
                heading_style
            )
        )

        story.append(
            Paragraph(
                "Detailed question-by-question analysis of the interview.",
                body_style
            )
        )

        story.append(
            Spacer(
                1,
                15
            )
        )

        for index, interview_question in enumerate(
            interview_questions
        ):

            question_number = index + 1

            if index < len(
                interview_answers
            ):

                interview_answer = (
                    interview_answers[index]
                )

            else:

                interview_answer = (
                    "Not Available"
                )

            if index < len(
                interview_evaluations
            ):

                interview_evaluation = (
                    interview_evaluations[index]
                )

            else:

                interview_evaluation = (
                    "Not Available"
                )

            if index < len(
                scores
            ):

                question_score = (
                    scores[index]
                )

            else:

                question_score = (
                    "N/A"
                )

            # -------------------------
            # Question Header
            # -------------------------

            story.append(
                Paragraph(
                    f"Question {question_number}",
                    heading_style
                )
            )

            story.append(
                Paragraph(
                    interview_question.replace(
                        "\n",
                        "<br/>"
                    ),
                    body_style
                )
            )

            story.append(
                Spacer(
                    1,
                    8
                )
            )

            # -------------------------
            # Candidate Answer
            # -------------------------

            story.append(
                Paragraph(
                    "Candidate Answer",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    interview_answer.replace(
                        "\n",
                        "<br/>"
                    ),
                    body_style
                )
            )

            story.append(
                Spacer(
                    1,
                    8
                )
            )

            # -------------------------
            # Score
            # -------------------------

            score_table = Table(
                [
                    [
                        "Question Score",
                        f"{question_score}/10"
                    ]
                ],
                colWidths=[
                    180,
                    180
                ]
            )

            score_table.setStyle(
                TableStyle(
                    [
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, -1),
                            colors.HexColor("#E8F1FF")
                        ),
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey
                        ),
                        (
                            "ALIGN",
                            (0, 0),
                            (-1, -1),
                            "CENTER"
                        ),
                        (
                            "VALIGN",
                            (0, 0),
                            (-1, -1),
                            "MIDDLE"
                        )
                    ]
                )
            )

            story.append(
                score_table
            )

            story.append(
                Spacer(
                    1,
                    8
                )
            )

            # -------------------------
            # AI Evaluation
            # -------------------------

            story.append(
                Paragraph(
                    "AI Evaluation",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    interview_evaluation.replace(
                        "\n",
                        "<br/>"
                    ),
                    body_style
                )
            )

            story.append(
                Spacer(
                    1,
                    20
                )
            )

            # -------------------------
            # Question Separator
            # -------------------------

            if (
                question_number
                <
                len(
                    interview_questions
                )
            ):

                story.append(
                    HRFlowable(
                        width="100%",
                        thickness=0.5,
                        color=colors.HexColor("#B0B0B0")
                    )
                )

                story.append(
                    Spacer(
                        1,
                        10
                    )
                )

    # -------------------------
    # Follow-up Section
    # -------------------------

    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor("#0F62FE")
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )

    story.append(
        Paragraph(
            "AI Follow-up Interview",
            heading_style
        )
    )

    story.append(
        Paragraph(
            followup_question.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )

    story.append(
        Paragraph(
            "Follow-up Answer",
            heading_style
        )
    )

    story.append(
        Paragraph(
            followup_answer.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )

    story.append(
        Paragraph(
            "Follow-up Evaluation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            followup_evaluation.replace(
                "\n",
                "<br/>"
            ),
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            30
        )
    )

    # -------------------------
    # AI Career Coach Section
    # -------------------------

    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor("#0F62FE")
        )
    )

    story.append(
        Spacer(
            1,
            15
        )
    )

    story.append(
        Paragraph(
            "🤖 AI Career Coach",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "Personalized career guidance based on your interview performance.",
            career_style
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )

    # -------------------------
    # Career Coach Content
    # -------------------------

    career_advice_lines = career_advice.split(
        "\n"
    )

    for line in career_advice_lines:

        line = line.strip()

        if not line:
            story.append(
                Spacer(
                    1,
                    6
                )
            )

            continue

        story.append(
            Paragraph(
                line,
                career_style
            )
        )

        story.append(
            Spacer(
                1,
                4
            )
        )

    story.append(
        Spacer(
            1,
            30
        )
    )

    # -------------------------
    # Footer
    # -------------------------

    story.append(
        HRFlowable(
            width="100%",
            thickness=0.8,
            color=colors.grey
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )

    story.append(
        Paragraph(
            "Generated by AI Mock Interview Platform",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            body_style
        )
    )

    # -------------------------
    # Build PDF
    # -------------------------

    pdf.build(
        story
    )