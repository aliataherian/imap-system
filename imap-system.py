import smtplib
import imaplib
import email
from email.header import decode_header
import traceback 
username= "your gmail" 
password = "password" 
imap_server= "imap.gmail.com" 
imap_port = 993
imap=imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)
status, messages = imap.select("INBOX")
N = 1
messages = int(messages[0])
for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding)
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
