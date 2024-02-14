import qrcode_function as fc
import smtplib
import email.message
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64

def make_message():
    mail_body = """
    <h1>Hello, here is your requested qrcode</h1>
    <p>Thank you for your trust! Yours sincerely.</p>
    """
    
    data = input("Enter your data to generate the qrcode:")
    img_path = fc.make_qrcode(data)
    
    message = MIMEMultipart()
    message['Subject'] = 'QR CODE GENERATED'
    message['From'] = 'origin_example@mail.com'
    message['To'] = 'destiny_example@mail.com'
    
    with open("password.json", "r") as json_file:
        loaded_data = json.load(json_file)
        password = loaded_data["pass"]
    
    message.attach(MIMEText(mail_body, 'html'))
    
    with open(img_path, "rb") as img_file:
        img_data = img_file.read()
        img_mime = MIMEImage(img_data, name=f"Qr_Code_{data}.png")
        message.attach(img_mime)
    
    return message, password
    
def access_server_mail(message, password):
    s = smtplib.SMTP('smtp.gmail.com: 587')
    
    s.starttls()
    s.login(message['From'], password)
    s.sendmail(message['From'], [message['To']], message.as_bytes())

# Uso das funções
email_message, email_password = make_message()
access_server_mail(email_message, email_password)
