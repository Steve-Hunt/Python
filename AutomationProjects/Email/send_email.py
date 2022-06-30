import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python"
sender_email = "stcrows@gmail.com"
receiver_email = "sph@huntnet.co.uk"
password = input("Password for " + sender_email+" :")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Success")


# This doesn't work now becasue Google will not let this kind of app access the email server
# for security reasons
#  
