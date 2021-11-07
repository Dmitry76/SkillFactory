import smtplib
import getpass
import os
from email.mime.text import MIMEText


def send_mail(receiver, subject, message):
    sender = "007.cebb@gmail.com"
    password = getpass.getpass("Пароль: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = "007"
        server.sendmail(sender, receiver, msg.as_string())

        return "Сообщение отправлено!"
    except Exception as _ex:
        return f"{_ex}\nОшибка!"


def main():
    receiver = input("Получатель: ")
    subject = input("Тема: ")
    message = input("Сообщение: ")
    print(send_mail(receiver=receiver, subject=subject, message=message))


if __name__ == "__main__":
    main()
