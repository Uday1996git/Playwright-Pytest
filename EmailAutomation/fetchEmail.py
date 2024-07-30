import email
import imaplib
import logging
from zipfile._path.glob import separate

from bs4 import BeautifulSoup
# import panda

user = "uday@revrr.digital"
password = "ndcs svnh pptw vcnh"
imap_url = "imap.gmail.com"


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def connect_to_gmail_imap():
    try:
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(user, password)
        mail.select('inbox')
        return mail
    except Exception as e:
        logging.error("Connection Failed: {}".format(e))
        raise


mails = connect_to_gmail_imap()
result, mail = mails.uid('search',  '(SUBJECT "Your One-Time Password (OTP) for Verification")')
mail_ids = mail[0]
id_list = mail_ids.split()
latest_email_id = id_list[-1]

result, data = mails.uid('fetch',latest_email_id, '(RFC822)')

email_message = email.message_from_bytes(data[0][1])

body = email_message.get_payload(decode=True)

parsed_body = BeautifulSoup(body, 'html.parser')
text = parsed_body.getText(separator='\n', strip=True)
print(text.split())
for i in text.split():
    if i.isnumeric():
        print(i)


# for num in ids_list:
#     typ, data = mails.fetch(num, '(RFC822)')
#     # if data[num].is_multipart:
#     print(num, email.message_from_bytes(data))
