import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"

class Email():
        def __init__(self):
            self.login = 'login@gmail.com'
            self.password = 'qwerty'
            self.subject = 'Subject'
            self.recipients = ['vasya@email.com', 'petya@email.com']
            self.message = 'Message'
            self.header = None

        def send_message(self):
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(self.recipients)
            msg['Subject'] = self.subject
            msg.attach(MIMEText(self.message))
            ms = smtplib.SMTP(GMAIL_SMTP, 587)
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            ms.login(self.login, self.password)
            ms.sendmail(self.login, ms, msg.as_string())
            ms.quit()

        def recieve(self):
            mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            mail.logout()

if __name__ == '__main__':
    email1 = Email()