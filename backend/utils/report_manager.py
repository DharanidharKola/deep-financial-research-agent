from pathlib import Path
from datetime import datetime

from backend.utils.pdf_generator import (
    create_pdf
)

REPORT_DIR = Path(
    "reports"
)

REPORT_DIR.mkdir(
    exist_ok=True
)


def save_report(

    report_text

):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_path = REPORT_DIR / (
        f"report_{timestamp}.pdf"
    )

    create_pdf(
        report_text,
        str(report_path)
    )

    return str(
        report_path
    )