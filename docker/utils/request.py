import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from io import BytesIO

def send_email(recv_email, df):
    sender_email = os.getenv("SENDER_EMAIL") 
    email_password = os.getenv("SENDER_EMAIL_PASSWORD")
    smtp_server = "smtp.naver.com"
    smtp_port = 587  # Change to 465 if you want to use SSL

    msg = MIMEMultipart()
    msg["Subject"] = "맛집 리스트를 전달드립니다"
    msg['From'] = sender_email
    msg['To'] = recv_email

    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False, engine='openpyxl')
    excel_buffer.seek(0)
    
    # Create an attachment
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(excel_buffer.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        'attachment; filename="data.xlsx"',
    )
    
    msg.attach(part)

    body = MIMEText("맛집 리스트 전달드립니다~!")
    msg.attach(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(sender_email, email_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
