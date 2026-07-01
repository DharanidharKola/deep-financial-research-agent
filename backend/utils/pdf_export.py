from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf(
    report_text,
    output_path
):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    story = [

        Paragraph(
            report_text.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    ]

    doc.build(story)