#!/usr/bin/python3

import smtplib
import ssl
import email
import datetime

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from gpiozero import CPUTemperature


cpu = CPUTemperature()
print(cpu.temperature)

if cpu.temperature >= 70:
    print('HOT HOT HOT')
    print('\nSending Email...\n')
    port = 465  # For SSL
    password = "SENDER EMAIL PASSWORD!"
    sender_email = "SENDER EMAIL"
    receiver_email = "RECIEVER EMAIL"
    message = """\
Subject: HEAT ALERT ({0}*C)

{1}

RPi4 CURRENTLY {0}*C""".format(cpu.temperature, datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'))

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("SENDER EMAIL", password)
        server.sendmail(sender_email, receiver_email, message)

    print('Email sent')
else:
    print('Temperature ok.')
