import smtplib, ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = ""
    password = ""
    receiver = ""
    contex = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=contex) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("Mail sent")