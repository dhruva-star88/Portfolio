import smtplib, ssl
import os


def send_email(message):
    # These both are standard values, which required for smtplib
    host = "smtp.gmail.com"
    port = 465

    user_name = "workdhruvateja@gmail.com"
    password = os.getenv("rev_portfolio")
    reciever = "dhruvatej6565@gmail.com"
    context = ssl.create_default_context()  # This is required to send emails securely

    # use with context manager to work with the above-mentioned parameters
    # context should be mentioned explicitly so that it can gain access, since to maintain parameters in order. For more info. go for implementation

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, reciever, message)
