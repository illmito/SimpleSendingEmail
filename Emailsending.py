import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "Test email coming from python code"
send_email = "jonnosmith1944@gmail.com"
receiver_email = "thomas.brayovic@gmail.com"
password = " " # ENTER PASSWORD.

message = EmailMessage()
message["From"] = send_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(send_email, password)
    server.sendmail(send_email, receiver_email, message.as_string())

print("Emailed sent.")

## this script is genneraly a miss when trying to execute, google accounts
## and most other providers no longer allow for this to work.