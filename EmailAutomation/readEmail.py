import imaplib, email

user = "uday@revrr.digital"
password = "ndcs svnh pptw vcnh"
imap_url = "imap.gmail.com"


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def get_emails(results_bytes):
    msgs=[]
    for num in results_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

    return msgs

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('Inbox')
msgs = get_emails(search('FROM','no-reply@revrr.ai', con))

# for msg in msgs[::-1]:
#     for sen
