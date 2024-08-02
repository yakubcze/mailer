import smtplib, ssl
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv # For .env files storing secrets

load_dotenv(find_dotenv()) # Load the .env file.

# Constants
port = 465  # For SSL
password = os.getenv("PASSWORD") # Password stored in .env file

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Create a secure SSL context
context = ssl.create_default_context()

def sendEmail(message_to_send, subject):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "Používáš e-mailový klient bez podpory HTML!"
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(message_to_send, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Print message, including header - debug
    #for key, value in message.items():
    #            print(f"{key}: {value}")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
