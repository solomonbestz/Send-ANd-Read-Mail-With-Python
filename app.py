from dotenv import load_dotenv

load_dotenv('.env')

def send_mail(text : str='Email Body', subject: str='Messsage From Solomon', to_emails:list =None) -> None:
    assert isinstance(to_emails, list)


if __name__=='__main__':
    ...