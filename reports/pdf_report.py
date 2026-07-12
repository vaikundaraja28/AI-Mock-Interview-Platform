from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    user,
    role,
    difficulty,
    question,
    answer,
    evaluation
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Mock Interview Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Candidate:</b> {user}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Role:</b> {role}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Difficulty:</b> {difficulty}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Interview Question</b>", styles["Heading2"]))
    story.append(Paragraph(question, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Your Answer</b>", styles["Heading2"]))
    story.append(Paragraph(answer, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>AI Evaluation</b>", styles["Heading2"]))
    story.append(Paragraph(evaluation.replace("\n", "<br/>"), styles["BodyText"]))

    pdf.build(story)