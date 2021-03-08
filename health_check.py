#!/usr/bin/env python3

import emails
import psutil
import shutil
import socket

# TODO: Change recipient
sender = "automation@example.com"
recipient = "username@example.com"
body = "Please check your system and resolve the issue as soon as possible."


def check_cpu():
    """Check CPU usage
    If CPU usage is over than 80%, report and send an email
    """
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        subject = "Error - CPU usage is over 80%"

        emails.generate_error_email(sender, recipient, subject, body)


def check_disk_space(disk):
    """Check disk space
    If disk space is less than 20%, report and send an email
    """
    available_disk_space = shutil.disk_usage(disk)
    free_space = available_disk_space.free / available_disk_space.total * 100
    if free_space < 20:
        subject = "Error - Available disk space is less than 20%"

        emails.generate_error_email(sender, recipient, subject, body)


def check_memory():
    """Check memory
    If available memory is less than 500 MB, report and send an email
    """
    available_memory = psutil.virtual_memory()
    limit = 500 * 1024 * 1024  # 500 MB

    if available_memory.available < limit:
        subject = "Error - Available memory is less than 500MB"

        emails.generate_error_email(sender, recipient, subject, body)


def check_localhost():
    """Check localhost
     if the hostname "localhost" cannot be resolved to "127.0.0.1", report and send an email
    """
    localhost = socket.gethostbyname('localhost')

    if localhost != '127.0.0.1':
        subject = "Error - localhost cannot be resolved to 127.0.0.1"

        emails.generate_error_email(sender, recipient, subject, body)


def main():
    check_cpu()
    check_disk_space("/")
    check_memory()
    check_localhost()


if __name__ == '__main__':
    main()
