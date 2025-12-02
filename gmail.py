print("Radhe Radhe...\n")
import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "er.ankityadav3gmail.com"
APP_PASSWORD = "radheji423@"
RECEIVER = "jat9928323@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Radhe Radhe ji jat sahab....."
msg.set_content("padai kesi chal rahi he......")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)