import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jeslyn2k5@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = "jeslyn2k5@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



