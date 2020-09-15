#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys #for pass parameters from bash
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

time = sys.argv[1]
server = 'smtp.e.mail' # <= here yr post provider's SMTP
user = 's@e.mail' # <= here yr mail
password = 'p@$$w0rd' # <= here yr password

recipients = 'r1@e.mail' # <= here we can add recipient or list of recipients, for example: recipients = ['r1@e.mail', 'r2@e.mail']
sender = 's@e.mail' #here u need paste yr email
subject = 'Delay'
text = 'Sorry, Im delay on '+time+' minutes'
html = '<html><head></head><body><p>'+text+'</p><br>--<p><b>This is an automated message - please do not reply to this message.</b></p><p>Best regards,</p><p>Name Surname</p><p>@ <a href="mailto:s@e.mail">s@e.mail</a></p><p>✆ <a href="tel:+1234567890">+1(234)567-890</a></p></body></html>'

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Name Python Delivery <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/'+(python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')

msg.attach(part_text)
msg.attach(part_html)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()
