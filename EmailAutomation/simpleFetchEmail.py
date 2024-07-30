import email
import imaplib
import logging
from bs4 import BeautifulSoup

user = "uday@revrr.digital"
password = "ndcs svnh pptw vcnh"
imap_url = "imap.gmail.com"


def remove_html_tags(body):
    parsed_body = BeautifulSoup(body, 'html.parser')
    text = parsed_body.getText(separator='\n', strip=True)
    return text


def retrun_OTP(body):
    for i in body.split():
        if i.isnumeric():
            return i


def connect_to_gmail_imap():
    try:
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(user, password)
        mail.select('inbox')
        return mail
    except Exception as e:
        logging.error("Connection Failed: {}".format(e))
        raise


def fetch_latest_email_by_subject(subject):
    mails = connect_to_gmail_imap()
    # search_query = f'(FROM "{subject}")'
    search_query = f'SUBJECT "{subject}"'
    typ, data = mails.search(None, search_query)
    # print(data[0].split()[-1])
    # typ, data = mails.uid('fetch', data[0].split()[-1], '(RFC822)')
    typ, data = mails.fetch(data[0].split()[-1], '(RFC822)')
    fina_body = remove_html_tags(email.message_from_bytes(data[0][1]).get_payload(decode=True))
    # print(retrun_OTP(fina_body))
    return retrun_OTP(fina_body)


def OTP_array(otp):
    # OTP = fetch_latest_email_by_subject("OTP")
    print(otp)
    count = len(otp)
    li = {}
    while int(otp) != 0:
        li[count] = int(otp) % 10
        # li.insert(count, int(OTP)%10)
        otp = int(otp) / 10
        count -= 1
    return li


# fetch_latest_email_by_subject("no-reply@revrr.ai")


# print(li)
# count = 0
if __name__ == "__main__":
    dic = OTP_array(fetch_latest_email_by_subject("Your One-Time Password (OTP) for Verification"))

    for count in range(1, len(dic)+1):
        print(dic[count])
# for count in range(1, len(li)+1):
#     print(li[count])
