#!/usr/bin/env python3

import datetime
import emails
import os
import re
import reports


def process_text_file(text_file):
    """Process text file to take only name and weight
    :param text_file: Text file
    :return: List of sentences of name and weight
    """

    processed_text = []
    desc_keys = ["name", "weight"]

    # Open file
    with open(text_file, 'r') as opened_file:
        # Iterate through sentences
        for index, sentence in enumerate(opened_file.readlines()):
            if index >= 2:
                break
            sentence = "{}: {}".format(desc_keys[index], sentence.strip())
            # Append sentence
            processed_text.append(sentence)

    return processed_text


def make_summary():
    """Iterate through descriptions folder to take the content
    :return: Summary from all of descriptions
    """
    summary = ""
    desc_dir = os.path.join("supplier-data", "descriptions")
    text_file_name_pattern = r"([0-9]+).txt$"

    for file in os.listdir(desc_dir):
        try:
            # Search file name in desc_dir
            result = re.search(text_file_name_pattern, file)

            # If there is the result, ...
            if result:
                file_path = os.path.join(desc_dir, file)
                # Process text file
                summary += "<br/>".join(process_text_file(file_path))

            summary += "<br/><br/>"  # Make 2 new lines
        except AttributeError:
            continue

    return summary


def main():
    """Generate PDF and send email"""
    file_name = "processed.pdf"

    # TODO: Choose OS
    # For Windows
    # pdf_dest_dir = os.path.join(os.path.abspath("/"), os.getcwd(), "tmp")

    # For Linux
    pdf_dest_dir = os.path.join(os.path.abspath("/"), "tmp")

    # Make destination directory
    if not os.path.exists(pdf_dest_dir):
        os.makedirs(pdf_dest_dir)

    pdf_file_path = os.path.join(pdf_dest_dir, file_name)

    # Generate PDF
    today = datetime.datetime.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
    summary = make_summary()

    reports.generate_report(pdf_file_path, title, summary)

    # Generate email
    # TODO: Change recipient
    sender = "automation@example.com"
    recipient = "student-01-fb49a5a2b556@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, recipient, subject, body, pdf_file_path)
    # Send email
    emails.send_email(message)


if __name__ == '__main__':
    main()
