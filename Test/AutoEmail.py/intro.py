import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = ''
password = ''

receiver_email = ""
subject = "Test Email"
body = "This is a test email sent from Python!" 

server=smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(sender_email,password)
print("Login Success")


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

server.sendmail(sender_email, receiver_email, message.as_string())