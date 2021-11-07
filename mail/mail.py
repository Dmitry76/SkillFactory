# import os
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receiver, subject, message, at_file):
    sender = "007.cebb@gmail.com"
    password = getpass.getpass("Пароль: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open(f"C:\\Users\\Asus\\PycharmProjects\\SkillFactory\\SkillFactory\\mail\\{message}") as file:
            content = file.read()
    except IOError:
        return "Ошибка обращения к файлу!"

    try:
        server.login(sender, password)
        # msg = MIMEText(message)
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = "007"
        msg.attach(MIMEText(content))

        if at_file == "":  # ЕСЛИ ПУТЬ К ВЛОЖЕНИЮ НЕ ПУСТОЙ, ТО ПРИКРЕПЛЯЕМ
            pass
        else:
            with open(f"C:\\Users\\Asus\\PycharmProjects\\SkillFactory\\SkillFactory\\mail\\{at_file}") as f:
                attach_file = MIMEText(f.read())
                attach_file.add_header('content-disposition', 'attachment', filename=at_file)
                msg.attach(attach_file)

        server.sendmail(sender, receiver, msg.as_string())

        return "Сообщение отправлено!"
    except Exception as _ex:
        return f"{_ex}\nОшибка!"


def main():

    receiver = input("Получатель: ")
    subject = input("Тема: ")
    message = input("Сообщение: ")
    at_file = input("Вложение: ")
    print(send_mail(receiver=receiver, subject=subject, message=message, at_file=at_file))


if __name__ == "__main__":
    main()
