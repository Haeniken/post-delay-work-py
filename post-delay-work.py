#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# First: export envs
# export SMTP_SERVER="smtp.e.mail"
# export SMTP_USER="s@e.mail"
# export SMTP_PASSWORD="p@$$w0rd"
# export SENDER_EMAIL="s@e.mail"
# export SENDER_NAME="Python Delivery"

# Second: run script
# python script.py 15 --recipients r1@e.mail,r2@e.mail

import argparse
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

# Загрузка конфигурации из переменных окружения
def load_config():
    return {
        'smtp_server': os.getenv('SMTP_SERVER', 'smtp.e.mail'),
        'smtp_user': os.getenv('SMTP_USER', 's@e.mail'),
        'smtp_password': os.getenv('SMTP_PASSWORD', 'p@$$w0rd'),
        'sender_email': os.getenv('SENDER_EMAIL', 's@e.mail'),
        'sender_name': os.getenv('SENDER_NAME', 'Name Python Delivery'),
    }

def create_message(sender, recipients, subject, text, html):
    """Создание MIME-сообщения."""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"{sender['name']} <{sender['email']}>"
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender['email']
    msg['Return-Path'] = sender['email']
    msg['X-Mailer'] = f"Python/{python_version()}"

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    return msg

# Отправка электронного письма
def send_email(server, user, password, sender, recipients, message):
    try:
        with smtplib.SMTP_SSL(server) as mail:
            mail.login(user, password)
            mail.sendmail(sender['email'], recipients, message.as_string())
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")

# Парсинг аргументов командной строки
def main():
    parser = argparse.ArgumentParser(description="Отправка уведомления о задержке.")
    parser.add_argument('time', type=str, help="Время задержки в минутах")
    parser.add_argument('--recipients', type=str, required=True, help="Список получателей через запятую")
    args = parser.parse_args()

# Загрузка конфигурации
    config = load_config()

# Подготовка данных
    time = args.time
    recipients = [email.strip() for email in args.recipients.split(',')]
    sender = {
        'email': config['smtp_user'],
        'name': config['sender_name']
    }
    subject = 'Delay'
    text = f"Sorry, I'm delayed by {time} minutes."
    html = f"""
    <html>
    <head></head>
    <body>
        <p>{text}</p>
        <br>
        --
        <p><b>This is an automated message - please do not reply to this message.</b></p>
        <p>Best regards,</p>
        <p>{sender['name']}</p>
        <p>@ <a href="mailto:{sender['email']}">{sender['email']}</a></p>
        <p>✆ <a href="tel:+1234567890">+1(234)567-890</a></p>
    </body>
    </html>
    """

# Создание и отправка сообщения
    message = create_message(sender, recipients, subject, text, html)
    send_email(
        server=config['smtp_server'],
        user=config['smtp_user'],
        password=config['smtp_password'],
        sender=sender,
        recipients=recipients,
        message=message
    )

if __name__ == "__main__":
    main()
