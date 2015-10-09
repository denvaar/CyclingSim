from src.version2.my_email import Email

class CheaterEmailer(Email):
    '''
    Sends an email that is specifically about the cheaters.
    '''
    def __init__(self, toBeDecorated):
        # The Email object to be decorated.
        self.decoratedEmail = toBeDecorated
    
    def doEmail(self, updatedObjects):
        # This method formats the body text
        # with the given updated racers that
        # might be cheating.
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
                h1 {
                    color: red;
                }
          </style>
         </head>
         <body>
          <h1>Alert!</h1>
          <h3>The following racers look suspicious and might be cheating.</h3>
          <br>
          <table>
           <th>Racers</th>
           <th>Times</th>"""
        for racer in updatedObjects:
            text = text + """<tr><td>%s and %s</td><td>%s and %s</td></tr>""" % \
                (str(racer[0].getBibAndName()) + "(team: " + str(racer[0].getTeam()) + ")",
                str(racer[1].getBibAndName()) + "(team: " + str(racer[1].getTeam()) + ")",
                str(racer[0].getPrettyTime()), str(racer[1].getPrettyTime()))
        text = text + """</table></body></html>"""
        
        self.sendEmail(text)

    # =============================
    # Overriden methods
    # =============================

    def sendEmail(self, body_txt):
        # Call the decorated email's sendEmail method
        # with the appropriate body text.
        self.decoratedEmail.sendEmail(body_txt)

