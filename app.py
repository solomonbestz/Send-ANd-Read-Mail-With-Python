from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib

load_dotenv('.env')

def send_mail(text : str='Email Body', subject: str='Messsage From Solomon', from_email:str =f'Solomon Azowenu<{os.getenv('username')}>', to_emails:list =None) -> None:
    assert isinstance(to_emails, list)

    msg: object = MIMEMultipart('alternative')
    msg['From'] =  from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject
    
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText('<h1>This is working </h1>', 'html')
    msg.attach(html_part)

    msg_str = msg.as_string()

    with smtplib.SMTP(host=host, port=port, timeout=120) as server:
        server.ehlo()
        server.starttls()
        server.login("YOUR USERNAME", "YOUR PASSWORD")
        server.sendmail(from_email, to_emails, msg_str)


if __name__=='__main__':
    host: str = os.getenv('host')
    port: int = os.getenv('port')


    send_mail(to_emails=["ugochukwuazowenu@gmail.com"])

    