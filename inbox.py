import email
import imaplib



if __name__=='__main__':

    host: str = 'imap.gmail.com'
    username: str = 'kingsolodawarrior@gmail.com'
    password: str = 'jwax jsbz pzoa wtni'

    mail: object = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select('inbox')

    _, search_data = mail.search(None, 'UNSEEN')

    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        a, b = data[0]
        # msg_str = str(b.decode('utf-8'))
        # print(msg_str)
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                print(part)
        input()
