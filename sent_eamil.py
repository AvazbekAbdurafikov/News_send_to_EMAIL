import smtplib,ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "Your Password"
    password = "Your app password from google"
    receiver = ""
    contex = ssl.create_default_context()
#     message = """
# Hi
# How are you?
# Bye!
# """
    with smtplib.SMTP_SSL(host=host, port=port, context=contex) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("Mail sent")