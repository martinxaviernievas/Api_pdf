import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario: str, contenido: str):
    