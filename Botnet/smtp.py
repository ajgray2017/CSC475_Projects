class SMTP:
    def __init__(self, sender, receiver, password):
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.port = 465
        self.payloadName = ""
        self.subject = "S TEST"
        self.contents = "C TEST"

    def getPayload(self):
        #todo add in filename from server
        #return input("Enter FileName: ")
        return "email_body.txt"

    def sendEmail(self):
        import smtplib, ssl, pickle
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject

        message.attach(MIMEText(self.contents, 'plain'))

        try:
            attachedFile = open(self.getPayload(), 'rb')
        except:
            #Todo Add in send back to server error, reinput file
            print("could not find file.. Try again.")
            self.sendEmail()

        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attachedFile).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename=self.payloadName)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender, self.password)

        text = message.as_string()
        session.sendmail(self.sender, self.receiver, self.contents)
        session.quit()
        
        return True

if __name__ == "__main__":
    import pickle
    smtp = SMTP(sender, receiver, password)
    SMTP.__module__ = "smtp"