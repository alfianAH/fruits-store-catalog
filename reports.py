#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, body):
    """Generate PDF
    :param attachment: File path
    :param title: Title of the fi;e
    :param body: Body of the file
    :return:
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    # Add title and body
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body, styles["BodyText"])
    # Build report
    report.build([report_title, report_body])
