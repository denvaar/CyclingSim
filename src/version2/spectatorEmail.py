import wx
import smtplib
#import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.version2.my_email import Email

class SpectatorEmail(Email):
    '''
    This class sends an email that is formatted
    for specators to revieve race updates.
    '''
    def __init__(self, toBeDecorated):
        self.decoratedEmail = toBeDecorated

    def sendEmail(self, body_txt):
        self.decoratedEmail.sendEmail(body_txt)

    def doEmail(self, updatedObjects):
        text = """
        <html>
         <head>
          <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                    text-align: left;    
                }
          </style>
         </head>
         <body>
          <h3>You've signed up to recieve updates for the following racers:</h3>
          <br>
          <table>
           <th>Racer</th>
           <th>Time</th>
           <th>Distance</th>"""
        for racer in updatedObjects:
            text = text + """<tr><td>%s</td><td>%s</td><td>%s</td></tr>""" % \
                (str(racer.getBibAndName()), str(racer.getPrettyTime()), str(racer.getSensor()))
        text = text + """</table></body></html>"""
        
        self.sendEmail(text)
