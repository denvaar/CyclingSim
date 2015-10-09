import smtplib
#import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.version2.emailer import Emailer

class Email(Emailer):
    def __init__(self, emailAddr):
        Emailer.__init__(self)
        self.emailAddr = emailAddr

    def sendEmail(self, body_txt):
        print "sending email to", self.emailAddr

        html_body = MIMEText(body_txt, 'html')
        msg = MIMEMultipart('alternative')
        msg['To'] = self.emailAddr
        msg['From'] = 'cs5700fall2015students@outlook.com'
        msg['Subject'] = 'Race Updates'
        msg.attach(html_body)
        server = smtplib.SMTP('mail.usu.edu')
        server.set_debuglevel(1)
        try:
            server.sendmail('cs5700fall2015students@outlook.com', self.emailAddr, msg.as_string())
        finally:
            server.quit() 

        print "...finished"
