import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'denverpsmith@gmail.com'))
msg['From'] = email.utils.formataddr(('Cycling Simulation', 'denverpsmith@gmail.com'))
msg['Subject'] = 'Race Updates'

server = smtplib.SMTP('mail')
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('denverpsmith@gmail.com', ['denverpsmith@gmail.com'], msg.as_string())
finally:
    server.quit()
